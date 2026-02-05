import logging
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

INPUT_FILE = "data/raw/patient_data.csv"
OUTPUT_FILE = "data/processed/clean_output.csv"
LOG_FILE = "logs/etl.log"

# Logging configuration
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_etl():
    logging.info("ETL started")

    df = extract_data(INPUT_FILE)
    logging.info(f"Extracted {len(df)} records")

    df_clean = transform_data(df)
    logging.info(f"Transformed to {len(df_clean)} records")

    load_data(df_clean, OUTPUT_FILE)
    logging.info("Data loaded successfully")

    print("✅ ETL pipeline completed successfully")

if __name__ == "__main__":
    run_etl()