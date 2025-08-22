import pandas as pd
from config.config import get_data_path

def save_raw(df: pd.DataFrame, file_name: str):
    path = get_data_path(file_name, processed=False)
    df.to_csv(path, index=False)
    return path

def save_processed(df: pd.DataFrame, file_name: str):
    path = get_data_path(file_name, processed=True)
    df.to_csv(path, index=False)
    return path
