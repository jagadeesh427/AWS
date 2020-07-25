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
    
    
#uploading file to s3

s3.meta.client.upload_file('/Users/jagadeeshyadav/people.csv', "jagadeesh427", "people.csv")
