
def list_s3_files(bucket_name: str):
    return {
        "message": "Mock S3 files listed successfully",
        "bucket_name": bucket_name,
        "files": ["report.pdf", "logs.txt", "backup.zip"]
    }
def list_s3_buckets():
    return {
        "message": "S3 buckets listed successfully (mock)",
        "buckets": [
            "project-data-bucket",
            "logs-storage-bucket",
            "backup-archive-bucket"
        ]
    }

