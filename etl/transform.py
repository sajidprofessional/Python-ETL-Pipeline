import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    df = df.dropna(subset=["amount"])
    df = df[df["status"] == "PAID"]
    return df
