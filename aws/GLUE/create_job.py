from datetime import datetime
import boto3
import json

default = {'region_name': 'us-east-1'}

glue_client = boto3.client('glue', **default)
iam_clinet = boto3.resource('iam')
s3_client = boto3.client('s3')


name_role_select = 'AWSGlueServiceRoleDefault'
bucket_code = 'aws-glue-scripts-771306241722-us-east-1'
key_path_code =  'root/victor.py'

try:
	role = iam_clinet.Role(name_role_select)
	tags = role.tags[0]
	tags = {tags['Key']: tags['Value']}

	if tags['fisrt'] != 'Glue':
		raise

except:
	print("Rol seleccionado no habilitado")
else:
	print(role.role_name,  ' Habilitado')

	response = s3_client.list_objects_v2(
	    Bucket=bucket_code,
	    MaxKeys=1,
	    Prefix=key_path_code
	)

	if response['KeyCount'] > 0:
		name_job = 'JobProof_{}'.format(str(datetime.now()))
		name_etl = 'GlueEtl_{}'.format(str(datetime.now()))

		new_job = glue_client.create_job(
			Name=name_job, 
			Role=name_role_select,
			Command={
				'Name': name_etl,
				'ScriptLocation': 's3://{}/{}'.format(bucket_code, key_path_code)
				}
			)
		print(new_job)
	else:
		print("PATH DE CODIGO NO LOCALIZADO")

