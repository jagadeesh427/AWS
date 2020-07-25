#mkdir ~/.aws
#cd .aws
#aws configure
#AWS Access Key Id: Enter key ID
#AWS Secret Access Key: enter the access Key

import boto3
#boto3.set_stream_logger('botocore', level='DEBUG')
s3= boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)
