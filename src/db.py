import psycopg2
from io import StringIO
import pandas as pd

def copy_to_postgres(df: pd.DataFrame, table_name: str, db_config: dict):
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    buffer = StringIO()
    df.to_csv(buffer, index=False, header=False)
    buffer.seek(0)

    cursor.copy_expert(
        f"""
        COPY {table_name}
        FROM STDIN
        WITH CSV
        """,
        buffer
    )

    conn.commit()
    cursor.close()
    conn.close()
