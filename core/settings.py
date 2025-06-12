import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# MLflow
MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5000")
MLFLOW_EXPERIMENT_DEFAULT = os.getenv("MLFLOW_EXPERIMENT_DEFAULT", "default")

# MinIO
MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT", "http://localhost:9000")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY", "minioadmin")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY", "minioadmin123")
MINIO_BUCKET_DATASETS = os.getenv("MINIO_BUCKET_DATASETS", "datasets")
MINIO_BUCKET_ARTIFACTS = os.getenv("MINIO_BUCKET_ARTIFACTS", "mlflow-artifacts")

# PostgreSQL
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_DB = os.getenv("POSTGRES_DB", "mlflow_db")
POSTGRES_USER = os.getenv("POSTGRES_USER", "mlflow_user")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "contrasena_segura")
POSTGRES_URI = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
    f"{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)
