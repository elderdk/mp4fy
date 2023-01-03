import json
from downloader import download
from boto3_handler import upload
from exceptions import VideoTooBigError


def handler(event, context):
    print(event)
    
    try:
        filename, info = download(event['queryStringParameters']['url'])
        signed_url = upload(filename)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'signed_url': signed_url,
                'info': info
            }),
            'headers': {'Content-Type': 'application/json'}}

    except VideoTooBigError as e:
        return {'statusCode': 461,
                'body': json.dumps({
                    'error': f"{e}"
                })
                }
    


if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=mgQqKeiL9c8"
    long_video_url = "https://www.youtube.com/watch?v=BcbmFxbdsJ0&ab_channel=%EB%AA%BD%ED%82%A4%EB%B9%84%EC%A7%80%EC%97%A0MONKEYBGM"
    result = handler({"queryStringParameters": {'url': url}}, {})
    print(result)