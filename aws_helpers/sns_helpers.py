#!/usr/bin/env python3
"""
    Purpose:
        Helper Library for AWS SNS Service. Will provide a
        functions for interacting with the Resource and Client
        APIs through Boto3
"""

# Python Library Imports
import logging
import boto3
from botocore.exceptions import ClientError, NoCredentialsError, BotoCoreError

###
# Manage SNS Resource Functions
###


def create_sns_resource(region_name=None, access_key=None, secret_key=None):
    """
    Purpose:
        Return a SNS resource object.
    Args:
        region_name (String): Name of region to connect to
        access_key (String): access key to use to connect to SNS Resource
        secret_key (String): secret key to use to connect to SNS Resource
    Return:
        dynamodb (SNS Resource Object): SNS Resource Object
    """

    sns = None
    try:
        if region_name:
            if access_key and secret_key:
                session = boto3.Session(
                    aws_access_key_id=access_key, aws_secret_access_key=secret_key
                )
                sns = session.resource("sns", region_name)
            else:
                sns = boto3.resource("sns", region_name)
        else:
            if access_key and secret_key:
                session = boto3.Session(
                    aws_access_key_id=access_key, aws_secret_access_key=secret_key
                )
                sns = session.resource("sns")
            else:
                sns = boto3.resource("sns")
    except NoCredentialsError as err:
        logging.exception("No Credentials Found for AWS")
        raise

    return sns


###
# Topic Management Function
###


def get_topic(sns, topic_arn):
    """
    Purpose:
        Return an SNS Topic by ARN
    Args:
        sns (SNS Resource Object): SNS Object owning the Topic
        topic_arn (String): ARN of the Topic
    Return:
        topic (SNS Topic Object): Topic object for the topic in
            SNS
    """

    try:
        return sns.Topic(topic_arn)
    except Exception as err:
        logging.exception(f"Exception Getting Topic: {err}")
        raise


###
# Email Topic Functions
###


def send_email_notification(topic, email_subject, email_msg):
    """
    Purpose:
        Send an email notification utilizing the SNS service
    Args:
        topic (SNS Topic Object): Topic object for the bucket in
            SNS
        email_subject (String): Subject of the email
        email_msg (String): Message Body of the email
    Return:
        N/A
    """

    try:
        topic.publish(Subject=email_subject, Message=email_msg)
    except Exception as err:
        logging.exception(f"Exception Publising Email Notification: {err}")
        raise
