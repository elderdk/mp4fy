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
    url = "https://www.youtube.com/watch?v=l05wkkCCe2Y&ab_channel=%EB%85%B8%EB%A7%88%EB%93%9C%EC%BD%94%EB%8D%94NomadCoders"
    long_video_url = "https://www.youtube.com/watch?v=BcbmFxbdsJ0&ab_channel=%EB%AA%BD%ED%82%A4%EB%B9%84%EC%A7%80%EC%97%A0MONKEYBGM"
    one_half_hour = "https://www.youtube.com/watch?v=alLs9S4pwo0&ab_channel=%EA%B5%AD%EA%B0%80%EC%97%B0%EA%B8%88%EC%88%A0%EC%82%AC"
    result = handler({"queryStringParameters": {'url': one_half_hour}}, {})
    print(result)