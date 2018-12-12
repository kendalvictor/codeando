from datetime import datetime
import boto3
import json

s3_client = boto3.client('s3')
dicc = {}
for _ in range(10000):
	dicc['date_created'] = str(datetime.now())
	dicc['num'] = _ 
	dicc_result = s3_client.put_object(
        ContentType='application/json',
        Body=json.dumps(dicc),
        Bucket='first-glue',
        Key='data/{}.json'.format(_)
    )
	print(dicc_result)


