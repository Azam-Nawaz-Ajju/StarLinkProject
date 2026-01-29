import pandas as pd

def load_excel_data(FILE_PATH: str) -> pd.DataFrame:
    df = pd.read_excel(FILE_PATH, header=0)
    df.columns = df.columns.str.strip()

    print("Columns:", df.columns.tolist())
    print("Rows loaded:", len(df))

    return df
