# Contains functions to control EC2 instances (start/stop/status)
# Handles EC2 operations such as starting an instance

import boto3


def start_ec2_instance(instance_id: str):
    ec2 = boto3.client("ec2")

    response = ec2.start_instances(InstanceIds=[instance_id])

    return {
        "message": "EC2 instance start request sent successfully",
        "instance_id": instance_id,
        "response": response
    }