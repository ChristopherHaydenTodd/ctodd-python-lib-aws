#!/usr/bin/env python3
"""
    Purpose:
        Helper Library for AWS DynamoDB Service. Will provide a
        functions for interacting with the Resource and Client
        APIs through Boto3
"""

# Python Library Imports
import logging
import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError, NoCredentialsError, BotoCoreError

###
# Manage DynamoDB Resource Functions
###


def create_dynamodb_resource(region_name=None, access_key=None, secret_key=None):
    """
    Purpose:
        Return a DynamoDB resource object.
    Args:
        region_name (String): Name of region to connect to
        access_key (String): access key to use to connect to DynamoDB Resource
        secret_key (String): secret key to use to connect to DynamoDB Resource
    Return:
        dynamodb (DynamoDB Resource Object): DynamoDB Resource Object
    """

    dynamodb = None
    try:
        if region_name:
            if access_key and secret_key:
                session = boto3.Session(
                    aws_access_key_id=access_key, aws_secret_access_key=secret_key
                )
                dynamodb = session.resource("dynamodb", region_name)
            else:
                dynamodb = boto3.resource("dynamodb", region_name)
        else:
            if access_key and secret_key:
                session = boto3.Session(
                    aws_access_key_id=access_key, aws_secret_access_key=secret_key
                )
                dynamodb = session.resource("dynamodb")
            else:
                dynamodb = boto3.resource("dynamodb")
    except NoCredentialsError as err:
        logging.exception("No Credentials Found for AWS")
        raise

    return dynamodb


###
# Table Functions
###


def get_table(dynamodb, table_name):
    """
    Purpose:
        Return an DynamoDB Table by name
    Args:
        dynamodb (DynamoDB Resource Object): DynamoDB Object owning the Table
        table_name (String): Name of table to return
    Return:
        table (DynamoDB Table Object): Table object for the table in
            DynamoDB
    """

    try:
        return dynamodb.Table(table_name)
    except Exception as err:
        logging.exception(f"Exception Getting Table: {err}")
        raise


def get_table_names(dynamodb):
    """
    Purpose:
        Return an Table Names in DynamoDB
    Args:
        dynamodb (DynamoDB Resource Object): DynamoDB Object owning the Table
    Return:
        table_names (List of Strings): Name of tables in DynamoDB
    """

    return [table.name for table in dynamodb.tables.all()]


def create_table(dynamodb, table_name, partition_key, sort_key={}, rcu=15, wcu=5):
    """
    Purpose:
        Create an DynamoDB Table by name
    Args:
        dynamodb (DynamoDB Resource Object): DynamoDB Object owning the Table
        table_name (String): Name of table to return
        partition_key (Dict): Dict with name and type of the partition key
            e.g. {"name": "name_of_partition_key", "type": "S"}
        sort_key (Dict): Dict with name and type of the sort key
            e.g. {"name": "name_of_sort_key", "type": "S"}
        rcu (Int): Read Capacity Units for the table. Defaults to 15
        wcu (Int): Write Capacity Units for the table. Defaults to 5
    Return:
        table (DynamoDB Table Object): Created Table Object
    """
    logging.info(f"Creating Table {table_name} with RCU={rcu} and WCU={wcu}")

    key_schema = []
    attribute_definitions = []

    key_schema.append({"AttributeName": partition_key["name"], "KeyType": "HASH"})
    attribute_definitions.append(
        {"AttributeName": partition_key["name"], "AttributeType": partition_key["type"]}
    )
    if sort_key:
        key_schema.append({"AttributeName": sort_key["name"], "KeyType": "RANGE"})
        attribute_definitions.append(
            {"AttributeName": sort_key["name"], "AttributeType": sort_key["type"]}
        )

    logging.info(f"Key Schema: {key_schema}")
    logging.info(f"Attribute Definitions: {attribute_definitions}")

    try:
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=key_schema,
            AttributeDefinitions=attribute_definitions,
            ProvisionedThroughput={"ReadCapacityUnits": rcu, "WriteCapacityUnits": wcu},
        )
    except Exception as err:
        logging.exception(f"Exception Creating Table: {err}")
        raise

    return table


def delete_table(table):
    """
    Purpose:
        Delete an DynamoDB Table
    Args:
        table (DynamoDB Table Object): Table to delete
    Return:
        N/A
    """

    try:
        response = table.delete()
    except Exception as err:
        logging.exception(f"Exception Deleting Table: {err}")
        raise


def check_table_exists_and_active(dynamodb, table_name):
    """
    Purpose:
        Check if Table exists and is active. When a table is created,
        it is not yet active. Active will define the table as fully
        created.
    Args:
        dynamodb (DynamoDB Resource Object): DynamoDB Object owning the Table
        table_name (String): Name of table to check for
    Return:
        table_exists (Boolean): Whether or not the table exists in DynamoDB
        table_active (Boolean): Whether or not the table is active in DynamoDB (fully
            created and ready for use)
    """

    table_exists = False
    table_active = False
    try:
        table = get_table(dynamodb, table_name)
        table_exists = True
        if table.table_status == "ACTIVE":
            table_active = True
        else:
            table_active = False
    except ClientError as err:
        if err.response.get("Error").get("Code") == "ResourceNotFoundException":
            table_exists = False
            table_active = False
        else:
            logging.exception(f"ClientError When Getting Table: {err}")
            raise err
    except Exception as err:
        logging.exception(f"Exception When Getting Table: {err}")
        raise err

    return table_exists, table_active


###
# Record Functions
###


def insert_record(table, record):
    """
    Purpose:
        Insert single record into DynamoDB table
    Args:
        table (DynamoDB Table Object): Table object for the table in
            DynamoDB
        record (Dict): Single to insert/update in the table
    Return:
        N/A
    """

    try:
        table.put_item(Item=record)
    except Exception as err:
        logging.exception(f"Exception Inserting Record Into Table: {err}")
        raise


def insert_records(table, records):
    """
    Purpose:
        Batch insert records into database
    Args:
        table (DynamoDB Table Object): Table object for the table in
            DynamoDB
        records (List of Dict): List of records to insert/update in the
            table
    Return:
        N/A
    """

    try:
        with table.batch_writer() as batch:
            for record in records:
                batch.put_item(Item=record)
    except Exception as err:
        logging.exception(f"Exception Batch Inserting Records Into Table: {err}")
        raise


def delete_record(table, query):
    """
    Purpose:
        Delete single record into DynamoDB table
    Args:
        table (DynamoDB Table Object): Table object for the table in
            DynamoDB
        query (Dict): Delete specifications (field and values to match
            record and delete)
    Return:
        N/A
    """

    try:
        table.delete_item(Item=record)
    except Exception as err:
        logging.exception(f"Exception Deleting Record From Table: {err}")
        raise


def get_records(table, query):
    """
    Purpose:
        Return Records from a Table
    Args:
        table (DynamoDB Table Object): Table object for the table in
            DynamoDB
    Return:
        ?
    """

    # table.query(KeyConditionExpression=Key('userId').eq("testuser"))
    # table.query(
    #     IndexName=gsi_name,
    #     KeyConditionExpression=Key("City").eq(city)
    # )

    try:
        for record in records:
            response = table.get_item(Key=record)
            item = response["Item"]
    except Exception as err:
        logging.exception(f"Exception Inserting Records Into Table: {err}")
        raise

    return records
