"""
Week 14 Project

"""

import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Get all instances
instances = ec2.describe_instances()

# Extract the instance IDs from the response
instance_ids = [instance['InstanceId'] for reservation in instances['Reservations'] for instance in reservation['Instances']]

# Terminate the instances..
if instance_ids:
    ec2.terminate_instances(InstanceIds=instance_ids)
    print(f"All instances are being terminated.")
else:
    print("No instances found.")
