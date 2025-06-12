from minio import Minio
from core.settings import MINIO_ENDPOINT, MINIO_ACCESS_KEY, MINIO_SECRET_KEY, MINIO_BUCKET_DATASETS

def download_dataset(filename: str, local_path: str) -> None:
    client = Minio(
        endpoint=MINIO_ENDPOINT.replace("http://", "").replace("https://", ""),
        access_key=MINIO_ACCESS_KEY,
        secret_key=MINIO_SECRET_KEY,
        secure=MINIO_ENDPOINT.startswith("https")
    )
    client.fget_object(MINIO_BUCKET_DATASETS, filename, local_path)
