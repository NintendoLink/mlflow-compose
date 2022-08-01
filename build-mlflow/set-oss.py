from minio import Minio
import os
from utils import Log

# Create client with AK&SK.
s3_endpoint = "minio-host:9000"
s3_region = "us-east-1"
s3_user = os.environ.get("AWS_ACCESS_KEY_ID")
s3_passwd = os.environ.get("AWS_SECRET_ACCESS_KEY")

log = Log()
try:
    log.logger.info(f"create mlflow bucket,endpoint:{s3_endpoint},region:{s3_endpoint}")
    client = Minio(s3_endpoint,
                   s3_user,
                   s3_passwd,
                   secure=False)
    bucket_exist = client.bucket_exists('mlflow-bucket')
    # Make the bucket if it does not exists
    if not bucket_exist:
        client.make_bucket('mlflow-bucket')
except BaseException:
    # todo
    raise