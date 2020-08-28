import pandas as pd
import os

# PATHS
DATA_PATH = 'data/images/'
TRAIN_META = 'data/train.csv'
TEST_META = 'data/test.csv'


def get_train_meta():
    df = pd.read_csv(TRAIN_META)
    return df


def get_train_filenames():
    files = os.listdir(DATA_PATH)
    files = [DATA_PATH + x for x in files if 'Train' in x]
    print("No of files found = ", len(files))
    return files


def get_test_meta():
    df = pd.read_csv(TEST_META)
    return df


def get_test_filenames():
    files = os.listdir(DATA_PATH)
    files = [DATA_PATH + x for x in files if 'Test' in x]
    print("No of files found = ", len(files))
    return files
