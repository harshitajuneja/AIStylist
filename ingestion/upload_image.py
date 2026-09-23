import os
from pathlib import Path

from database import supabase


BUCKET = "fashion-products"


def upload_image(
    local_path: str,
    storage_path: str
):

    with open(local_path, "rb") as f:

        file_data = f.read()

    extension = Path(local_path).suffix.lower()

    content_type = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".webp": "image/webp"
    }.get(
        extension,
        "application/octet-stream"
    )

    supabase.storage \
        .from_(BUCKET) \
        .upload(
            storage_path,
            file_data,
            {
                "content-type": content_type,
                "upsert": "true"
            }
        )

    public_url = (
        supabase.storage
        .from_(BUCKET)
        .get_public_url(
            storage_path
        )
    )

    return public_url