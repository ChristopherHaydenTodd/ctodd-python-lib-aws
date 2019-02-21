#!/usr/bin/env python3
"""
    Purpose:
        Helper Library for AWS SQS Service. Will provide a
        functions for interacting with the Resource and Client
        APIs through Boto3
"""

# Python Library Imports
import logging
import boto3
from botocore.exceptions import ClientError, NoCredentialsError, BotoCoreError

###
# Manage SQS Resource Functions
###


def create_sqs_resource(region_name=None, access_key=None, secret_key=None):
    """
    Purpose:
        Return a SQS resource object.
    Args:
        region_name (String): Name of region to connect to
        access_key (String): access key to use to connect to SQS Resource
        secret_key (String): secret key to use to connect to SQS Resource
    Return:
        sqs (SQS Resource Object): SQS Resource Object
    """

    sqs = None
    try:
        if region_name:
            if access_key and secret_key:
                session = boto3.Session(
                    aws_access_key_id=access_key, aws_secret_access_key=secret_key
                )
                sqs = session.resource("sqs", region_name)
            else:
                sqs = boto3.resource("sqs", region_name)
        else:
            if access_key and secret_key:
                session = boto3.Session(
                    aws_access_key_id=access_key, aws_secret_access_key=secret_key
                )
                sqs = session.resource("sqs")
            else:
                sqs = boto3.resource("sqs")
    except NoCredentialsError as err:
        logging.exception("No Credentials Found for AWS")
        raise

    return sqs


###
# Queue Management Function
###


def get_queue(sqs, queue_name):
    """
    Purpose:
        Return an SQS Queue by Queue Name
    Args:
        sqs (SQS Resource Object): SQS Resource Object
        queue_name (String): Name of Queue
    Return:
        queue (SQS Queue Object): Queue object for the queue in
            SQS
    """

    try:
        return sqs.get_queue_by_name(QueueName=queue_name)
    except Exception as err:
        logging.exception(f"Exception Getting Queue: {err}")
        raise


###
# Message Management Functions
###


def get_messages(queue, max_msgs=10, wait_time=20, attr_names=["All"]):
    """
    Purpose:
        Get messages in an SQS Queue
    Args:
        queue (SQS Queue Object): Queue object for the queue in
            SQS
        max_msgs (Int): Max messages to pull at once
        wait_time (Int): Seconds to wait for a message if queues are empty
        attr_names (List of Strings): Filter for messages to pull (if applicable)
    Return:
        messages ()
    """

    try:
        return queue.receive_messages(
            MaxNumberOfMessages=max_msgs,
            WaitTimeSeconds=max_msgs,
            AttributeNames=attr_names,
        )
    except Exception as err:
        logging.exception(f"Exception Getting Messages: {err}")
        raise


def delete_message(msg):
    """
    Purpose:
        Delete Message an SQS Queue
    Args:
        msg (SQS Message Object): Message in SQS
    Return:
        N/A
    """

    try:
        msg.delete()
    except Exception as err:
        logging.exception(f"Exception Deleting Messages: {err}")
        raise
