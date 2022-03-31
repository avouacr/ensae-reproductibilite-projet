"""Import raw data."""
import os
import pandas as pd


def import_clean_data(dir_data):
    "Import raw data."
    training_data = pd.read_csv(os.path.join(dir_data, 'train.csv'))
    test_data = pd.read_csv(os.path.join(dir_data, 'test.csv'))
    return training_data, test_data
