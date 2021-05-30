#!/usr/bin/env python3
import sys
import boto3
import jsonify

BUCKET_NAME = 'guerysbucket'

s3_resources = boto3.resource('s3')
s3_client = boto3.client('s3')

def list_buckets():
 buckets = []
 for item in s3_resources.buckets.all():
     print(item.name)
     buckets.append(item.name)
     return s3_client.list_buckets()
def upload(file):

    s3_client.upload_file(file, BUCKET_NAME, file)

def delete_object(file_name,bucket):
    s3_resources.Object(bucket,file_name).delete()


