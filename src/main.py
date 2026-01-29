from config import FILE_PATH, DB_CONFIG, TABLE_NAME
from data_loader import load_excel_data
from data_cleaner import clean_retail_data
from db_loader import load_to_postgres

def run_pipeline():
    df_raw = load_excel_data(FILE_PATH)
    df_clean = clean_retail_data(df_raw)
    load_to_postgres(df_clean, DB_CONFIG, TABLE_NAME)

if __name__ == "__main__":
    run_pipeline()
