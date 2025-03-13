import os
import boto3
from google.cloud import storage

class Storage:
    def __init__(self, provider="AWS"):
        self.provider = provider

        if provider == "AWS":
            self.client = boto3.client(
                "s3",
                aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
                aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
            )
            self.bucket_name = os.getenv("AWS_BUCKET_NAME")

        elif provider == "GCS":
            self.client = storage.Client()
            self.bucket_name = os.getenv("GCS_BUCKET_NAME")

    def upload_file(self, file_path: str, dest_path: str):
        """Uploads file to S3/GCS bucket"""
        if self.provider == "AWS":
            self.client.upload_file(file_path, self.bucket_name, dest_path)
        else:
            bucket = self.client.bucket(self.bucket_name)
            blob = bucket.blob(dest_path)
            blob.upload_from_filename(file_path)

        return f"{self.provider}://{self.bucket_name}/{dest_path}"

# Example usage:
# storage = Storage(provider="AWS")
# print(storage.upload_file("localfile.txt", "uploads/remote.txt"))
