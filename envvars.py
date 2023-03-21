from .provider import CloudStorageProvider, GoogleCloudStorage, AmazonCloudStorage
from dotenv import load_dotenv
import io


class Manager:
    def __init__(self, envfile_path: str, provider: CloudStorageProvider = None):
        self.envfile_path = envfile_path
        self.provider = provider or self.get_provider_by_path()
        self.envfile_stream = self.provider.get_envfile(self.envfile_path)

        if self.envfile_stream.__class__.__name__ == 'BytesIO':
            string_data = self.envfile_stream.getvalue().decode()
            self.envfile_stream = io.StringIO(string_data)

    def get_provider_by_path(self) -> CloudStorageProvider:
        if self.envfile_path is None:
            raise ValueError('envfile_path is None')
        elif self.envfile_path.startswith('gs://'):
            return GoogleCloudStorage()
        elif self.envfile_path.startswith('s3://'):
            return AmazonCloudStorage()

    def load(self):
        load_dotenv(stream=self.envfile_stream)

def main():

    import os

    path = os.getenv("ENVFILE_PATH")
    print(f"ENVFILE_PATH: {path}")
    manager = Manager(path)
    manager.load()