import json
import requests

def lambda_handler(event, context):
    response = requests.get('https://httpbin.org/ip')
    ip = response.json()['origin']
    return {
        'statusCode': 200,
        'body': json.dumps(f'Your IP is {ip}')
    }
