import os
import tempfile
import requests
import pandas as pd

from database import supabase
from qwen.analyzer import analyze_image

from upload_image import upload_image


CSV_FILE = "data/products.csv"


def download_image(
    image_url: str,
    output_path: str
):

    response = requests.get(
        image_url,
        timeout=30
    )

    response.raise_for_status()

    with open(
        output_path,
        "wb"
    ) as f:

        f.write(
            response.content
        )


def insert_product(
    product_data,
    image_url
):

    row = {

        "external_id":
            product_data.get(
                "external_id"
            ),

        "name":
            product_data.get(
                "name"
            ) or "Unnamed Product",

        "image_url":
            image_url,

        "category":
            product_data.get(
                "category"
            ),

        "color":
            product_data.get(
                "color",
                []
            ),

        "silhouette":
            product_data.get(
                "silhouette"
            ),

        "neckline":
            product_data.get(
                "neckline"
            ),

        "pattern":
            product_data.get(
                "pattern"
            ),

        "print_scale":
            product_data.get(
                "print_scale"
            ),

        "fabric":
            product_data.get(
                "fabric"
            ),

        "occasion":
            product_data.get(
                "occasion",
                []
            ),

        "style":
            product_data.get(
                "style",
                []
            ),

        "destination":
            product_data.get(
                "destination",
                []
            ),

        "body_types":
            product_data.get(
                "body_types",
                []
            ),

        "undertones":
            product_data.get(
                "undertones",
                []
            ),

        "description":
            product_data.get(
                "description"
            )
    }

    result = (
        supabase
        .table("products")
        .insert(row)
        .execute()
    )

    return result


def process_csv():

    df = pd.read_csv(
        CSV_FILE
    )

    print(
        f"Found {len(df)} products"
    )

    for index, row in df.iterrows():

        external_id = str(
            row.get(
                "product_id",
                index
            )
        )

        image_url = row.get(
            "image_url"
        )

        if not image_url:

            print(
                f"Skipping {external_id}: "
                "no image URL"
            )

            continue

        print(
            f"\nProcessing {external_id}"
        )

        try:

            with tempfile.NamedTemporaryFile(
                suffix=".jpg",
                delete=False
            ) as temp:

                temp_path = temp.name


            # 1. Download image

            download_image(
                image_url,
                temp_path
            )


            # 2. Qwen analyzes image

            print(
                "Running Qwen..."
            )

            attributes = analyze_image(
                temp_path
            )


            # 3. Add original ID

            attributes[
                "external_id"
            ] = external_id


            # 4. Upload image

            storage_path = (
                f"dresses/{external_id}.jpg"
            )

            print(
                "Uploading image..."
            )

            public_url = upload_image(
                temp_path,
                storage_path
            )


            # 5. Insert database record

            insert_product(
                attributes,
                public_url
            )


            print(
                "Successfully inserted:",
                attributes.get("name")
            )


        except Exception as e:

            print(
                f"ERROR {external_id}:",
                e
            )

        finally:

            if os.path.exists(
                temp_path
            ):

                os.remove(
                    temp_path
                )


if __name__ == "__main__":

    process_csv()