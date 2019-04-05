

# Christopher H. Todd's Python Python Library For Interacting With AWS

The ctodd-python-lib-aws project is responsible for interacting with [Amazon Web Services](https://aws.amazon.com/developer/language/python/). This includes interacting with DynamoDB, Lambda, S3, SNS, and SQS, and will be expanded in the future.

The library relies on Python's boto3 package which is used to communicate with the AWS APIs and warps the code with exception handling, logging, and other useful and redundant code.

## Table of Contents

- [Dependencies](#dependencies)
- [Libraries](#libraries)
- [Example Scripts](#example-scripts)
- [Notes](#notes)
- [TODO](#todo)

## Dependencies

### Python Packages

- boto3>=1.7.32
- botocore>=1.12.71
- wrapt>=1.10.8

## Libraries

### [dynamodb_helpers.py](https://github.com/ChristopherHaydenTodd/ctodd-python-lib-aws/blob/master/aws_helpers/dynamodb_helpers.py)

Helper Library for AWS DynamoDB Service. Will provide a functions for interacting with the Resource and Client APIs through Boto3

Functions:

```
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
```

```
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
```

```
def get_table_names(dynamodb):
    """
    Purpose:
        Return an Table Names in DynamoDB
    Args:
        dynamodb (DynamoDB Resource Object): DynamoDB Object owning the Table
    Return:
        table_names (List of Strings): Name of tables in DynamoDB
    """
```

```
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
```

```
def delete_table(table):
    """
    Purpose:
        Delete an DynamoDB Table
    Args:
        table (DynamoDB Table Object): Table to delete
    Return:
        N/A
    """
```

```
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
```

```
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
```

```
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
```

```
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
```

```
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
```

### [lambda_helpers.py](https://github.com/ChristopherHaydenTodd/ctodd-python-lib-aws/blob/master/aws_helpers/lambda_helpers.py)

Helper Library for AWS Lambda Service. Will provide a functions for interacting with the Resource and Client APIs through Boto3

Functions:

```
def get_bucket_name_from_s3_event(event):
    """
    Purpose:
        Get the S3 Bucket name from an event triggered by the creation
        of an object in S3
    Args:
        event (Dict): Dict with event details from the triggering event
            for the function.
    Return:
        bucket_name (String): Bucket name of the object creation triggering
            the call to the Lambda function
    """
```

```
def get_object_key_from_s3_event(event):
    """
    Purpose:
        Get the S3 Bucket name from an event triggered by the creation
        of an object in S3
    Args:
        event (Dict): Dict with event details from the triggering event
            for the function.
    Return:
        bucket_name (String): Bucket name of the object creation triggering
            the call to the Lambda function
    """
```

### [s3_helpers.py](https://github.com/ChristopherHaydenTodd/ctodd-python-lib-aws/blob/master/aws_helpers/s3_helpers.py)

Helper Library for AWS S3 Service. Will provide a functions for interacting with the Resource and Client APIs through Boto3

Functions:

```
def create_s3_resource(region_name=None, access_key=None, secret_key=None):
    """
    Purpose:
        Return a S3 resource object.
    Args:
        region_name (String): Name of region to connect to
        access_key (String): access key to use to connect to S3 Resource
        secret_key (String): secret key to use to connect to S3 Resource
    Return:
        s3 (S3 Resource Object): S3 Resource Object
    """
```

```
def get_bucket(s3, bucket_name):
    """
    Purpose:
        Return an S3 Bucket by name
    Args:
        s3 (S3 Resource Object): S3 Object owning the Bucket
        bucket_name (String): Name of bucket to return
    Return:
        bucket (S3 Bucket Object): Bucket object for the bucket in
            S3
    """
```

```
def get_bucket_names(s3):
    """
    Purpose:
        Return an Bucket Names in S3
    Args:
        s3 (S3 Resource Object): S3 Object owning the Bucket
    Return:
        bucket_names (List of Strings): Name of buckets in S3
    """
```

```
def create_bucket(s3, bucket_name, region_name=None):
    """
    Purpose:
        Create an S3 Bucket by name
    Args:
        s3 (S3 Resource Object): S3 Object owning the Bucket
        bucket_name (String): Name of bucket to return
        region_name (String): Region to create bucket in
    Return:
        N/A
    """
```

```
def delete_bucket(bucket, force=True):
    """
    Purpose:
        Delete an S3 Bucket
    Args:
        bucket (S3 Bucket Object): Bucket to upload file to
        force (Boolean): Whether or not to delete all objects in
            the bucket to force the delete. If false, will try to
            delete and fail if there are objects in the bucket
    Return:
        N/A
    """
```

```
def download_file(bucket, key, filename=None):
    """
    Purpose:
        Download a File to an S3 bucket
    Args:
        bucket (S3 Bucket Object): Bucket to download file from
        key (String): Name of the object in S3
        filename (String): Path to the file on the local host
    Return:
        N/A
    """
```

```
def upload_file(bucket, key, filename, encryption=None):
    """
    Purpose:
        Upload a File to an S3 bucket
    Args:
        bucket (S3 Bucket Object): Bucket to upload file to
        key (String): Desired name of the object in S3
        filename (String): Path to the file on the local host
        encryption (String): Server Side Encryption Method
    Return:
        N/A
    """
```

```
def delete_all_files_in_bucket(bucket):
    """
    Purpose:
        Delete all files in a Bucket
    Args:
        bucket (S3 Bucket Object): Bucket to delete files from
    Return:
        N/A
    """
```

```
def generate_presigned_url(s3, bucket_name, key, url_expire=900):
    """
    Purpose:
        Return a presigned URL to a file
    Args:
        s3 (S3 Resource Object): S3 Resource Object
        bucket_name (String): Name of bucket in S3 with Object
        key (String): Name of the object in S3
        url_expire (int): Number of seconds for the URL to live
    Returns:
        presigned_url (String): Presigned URL
    """
```

### [sns_helpers.py](https://github.com/ChristopherHaydenTodd/ctodd-python-lib-aws/blob/master/aws_helpers/sns_helpers.py)

Helper Library for AWS SNS Service. Will provide a functions for interacting with the Resource and Client APIs through Boto3

Functions:

```
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
```

```
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
```

```
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
```

### [sqs_consumer.py](https://github.com/ChristopherHaydenTodd/ctodd-python-lib-aws/blob/master/aws_helpers/sqs_consumer.py)

SQS Consumer Class. Will provide functionality to consume from SQS Queues in AWS

Classes:

```
class SQSConsumer(object):
    """
        SQSConsumer Class
    """
```

Functions:

#### N/A

### [sqs_helpers.py](https://github.com/ChristopherHaydenTodd/ctodd-python-lib-aws/blob/master/aws_helpers/sqs_helpers.py)

Helper Library for AWS SQS Service. Will provide a functions for interacting with the Resource and Client APIs through Boto3

Functions:

```
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
```

```
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
```

```
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
```

```
def delete_message(msg):
    """
    Purpose:
        Delete Message an SQS Queue
    Args:
        msg (SQS Message Object): Message in SQS
    Return:
        N/A
    """
```


## Example Scripts

Example executable Python scripts/modules for testing and interacting with the library. These show example use-cases for the libraries and can be used as templates for developing with the libraries or to use as one-off development efforts.

### N/A
## Notes

 - Relies on f-string notation, which is limited to Python3.6.  A refactor to remove these could allow for development with Python3.0.x through 3.5.x

## TODO

 - Unittest framework in place, but lacking tests
