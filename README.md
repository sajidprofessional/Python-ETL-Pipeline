# Python ETL Pipeline

An end-to-end **ETL pipeline** built using Python to demonstrate real-world data engineering practices including **data validation**, **error handling**, **logging**, and **scheduler readiness**.

---

## Features

- Extracts CSV data from `data/raw/`
- Transforms and cleans healthcare-style records
- Validates schema and null values
- Loads processed data to `data/processed/`
- Logging of ETL steps in `logs/etl.log`
- Exception handling and retry-ready design
- Scheduler-ready (Windows Task Scheduler / Airflow-compatible structure)
- Modular Python package design

---

## Tech Stack

- Python 3.10+
- Pandas
- Logging
- SQL-ready design
- Windows Task Scheduler compatible

---

## Project Structure

python-etl-pipeline/
├── data/
│ ├── raw/
│ │ └── patient_data.csv
│ ├── processed/
│
├── etl/
│ ├── init.py
│ ├── extract.py
│ ├── transform.py
│ ├── load.py
│ └── main.py
│
├── logs/
│ └── etl.log
├── requirements.txt
└── README.md

---

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/sajidprofessional/python-etl-pipeline.git
cd python-etl-pipeline
2.Create a virtual environment
py -m venv venv
source venv/Scripts/activate   # Windows
