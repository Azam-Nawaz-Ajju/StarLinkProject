import psycopg2
from psycopg2.extras import execute_values

def load_to_postgres(df, db_config, table_name):

    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()

    cur.execute(f"DROP TABLE IF EXISTS {table_name};")

    cur.execute(f"""
        CREATE TABLE {table_name} (
            invoiceno TEXT,
            stockcode TEXT,
            description TEXT,
            quantity INTEGER,
            invoicedate TIMESTAMP,
            unitprice NUMERIC,
            customerid INTEGER,
            country TEXT,
            total_price NUMERIC
        );
    """)

    insert_query = f"""
        INSERT INTO {table_name} VALUES %s
    """

    execute_values(cur, insert_query, df.values.tolist())
    conn.commit()

    cur.close()
    conn.close()

    print("Data loaded into Supabase successfully")
