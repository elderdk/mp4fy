import json
from downloader import download
from boto3_handler import upload
from exceptions import VideoTooBigError


def handler(event, context):
    print(event)

    try:
        filename, info = download(event["queryStringParameters"]["url"])
        signed_url = upload(filename)

        return {
            "statusCode": 200,
            "body": json.dumps({"signed_url": signed_url, "info": info}),
            "headers": {"Content-Type": "application/json"},
        }

    except VideoTooBigError as e:
        return {"statusCode": 200, "body": json.dumps({"error": f"{e}"})}

    except Exception as e:
        return {"statusCode": 200, "body": json.dumps({"error": f"{e}"})}


if __name__ == "__main__":
    pass
