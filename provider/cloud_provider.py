class CloudStorageProvider:

    def get_envfile(self, envfile_path: str) -> str:
        pass

    def download_file(self, bucket_name: str, remote_file_path: str, local_file_path: str):
        pass

    def delete_file(self, bucket_name: str, remote_file_path: str):
        pass
