import pandas as pd

def extract_data(file_path: str) -> pd.DataFrame:
    """
    Extract data from CSV file
    """
    return pd.read_csv(file_path)