import os
import logging

from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INPUT_FILE = os.path.join(BASE_DIR, "data", "raw", "patient_data.csv")
OUTPUT_FILE = os.path.join(BASE_DIR, "data", "processed", "clean_output.csv")
LOG_FILE = os.path.join(BASE_DIR, "logs", "etl.log")

# Logging config
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def etl_pipeline():
    try:
        logging.info("ETL started")

        df = extract_data(INPUT_FILE)
        df_clean = transform_data(df)
        load_data(df_clean, OUTPUT_FILE)

        logging.info("ETL completed successfully")

    except Exception as e:
        logging.error(f"ETL failed: {e}")
        raise

if __name__ == "__main__":
    etl_pipeline()
