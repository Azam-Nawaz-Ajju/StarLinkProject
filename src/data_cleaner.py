import pandas as pd


def clean_retail_data(df):
    df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]
    df = df[df["Quantity"] > 0]
    df = df[df["UnitPrice"] > 0]
    df = df.dropna(subset=["CustomerID"])

    df["InvoiceDate"] = df["InvoiceDate"].astype("datetime64[ns]")
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

    print("Rows after cleaning:", len(df))
    return df


