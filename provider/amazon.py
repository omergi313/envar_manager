from boto3 import client
from .cloud_provider import CloudStorageProvider


class AmazonCloudStorage(CloudStorageProvider):
    def __init__(self):
        self.client = client('s3')

    def get_envfile(self, envfile_path: str) -> str:
        # Implementation for Google Cloud Storage
        pass

    def download_file(self, bucket_name: str, remote_file_path: str, local_file_path: str):
        # Implementation for Amazon Cloud Storage
        pass

    def delete_file(self, bucket_name: str, remote_file_path: str):
        # Implementation for Amazon Cloud Storage
        pass
