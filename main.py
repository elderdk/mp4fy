import json
from downloader import download
from boto3_handler import upload

def handler(event, context):

    filename, info = download(event['body'])
    
    signed_url = upload(filename)
    
    return {'statusCode': 200,
            'body': json.dumps({
                'signed_url': signed_url,
                'info': info
            }),
            'headers': {'Content-Type': 'application/json'}}

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=l05wkkCCe2Y&ab_channel=%EB%85%B8%EB%A7%88%EB%93%9C%EC%BD%94%EB%8D%94NomadCoders"
    handler({"body": url}, {})