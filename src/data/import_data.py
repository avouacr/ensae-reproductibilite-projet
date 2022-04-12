"""Import raw data."""
import os

import s3fs
import pandas as pd


def import_clean_data_s3(bucket, dir_data):
    "Import raw data."
    # Create filesystem object
    S3_ENDPOINT_URL = "https://" + os.environ["AWS_S3_ENDPOINT"]
    fs = s3fs.S3FileSystem(client_kwargs={'endpoint_url': S3_ENDPOINT_URL})

    # Import data in pandas
    train_path = os.path.join(bucket, dir_data, "train.csv")
    test_path = os.path.join(bucket, dir_data, "test.csv")
    with fs.open(train_path, mode="rb") as file_in:
        training_data = pd.read_csv(file_in)
    with fs.open(test_path, mode="rb") as file_in:
        test_data = pd.read_csv(file_in)

    return training_data, test_data

def import_clean_data(train_url, test_url):
    training_data = pd.read_csv(train_url)
    test_data = pd.read_csv(test_url)
    return training_data, test_data
