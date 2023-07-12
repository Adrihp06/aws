import boto3

sagemaker_runtime = boto3.client('sagemaker-runtime')
csv_line_predict = """I loved it!"""
ep_name = 'reviews-endpoint'

response = sagemaker_runtime.invoke_endpoint(EndpointName=ep_name,
                                             ContentType='text/csv',
                                             Accept='text/csv',
                                             Body=csv_line_predict)

response_body = response['Body'].read().decode('utf-8').strip()
print(response_body)