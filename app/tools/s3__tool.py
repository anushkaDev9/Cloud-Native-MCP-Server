# Contains functions to interact with AWS S3 (e.g., list bucket files)
# Handles S3 operations such as listing files in a bucket

import boto3


def list_s3_files(bucket_name: str):
    s3 = boto3.client("s3")

    response = s3.list_objects_v2(Bucket=bucket_name)

    files = []
    for obj in response.get("Contents", []):
        files.append(obj["Key"])

    return {
        "message": "S3 files listed successfully",
        "bucket_name": bucket_name,
        "files": files
    }