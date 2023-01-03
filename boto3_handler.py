import os
import boto3

s3_client = boto3.client(
    "s3",
    config=boto3.session.Config(
        s3={"addressing_style": "path"}, signature_version="s3v4"
    ),
)


def get_signed_url(filename, expiration):
    signed_url = s3_client.generate_presigned_url(
        "get_object",
        Params={"Bucket": os.environ["bucketname"], "Key": filename},
        ExpiresIn=expiration,
    )

    return signed_url


def upload(filename, objectname=None):

    if objectname is None:
        objectname = os.path.basename(filename)

    response = s3_client.upload_file(filename, os.environ["bucketname"], objectname)

    return get_signed_url(objectname, os.environ["expiration"])
