# StarLink Retail Sales Analysis – End-to-End Data Pipeline

This project demonstrates a complete **end-to-end data analytics pipeline** using a real-world retail dataset.

**Flow:**  
Excel → Python (ETL) → PostgreSQL (Supabase) → Looker Studio → GitHub

The objective is to clean raw transactional data, load it into a cloud PostgreSQL database, and visualize insights using Looker Studio.

---

## 1. Business Problem

A retail company wants to analyze its sales performance to:
- Identify sales trends over time
- Understand product and country-level performance
- Improve inventory and sales decisions

---

## 2. Dataset Overview

- Dataset Type: Transactional retail data
- Time Period: 01-12-2010 to 09-12-2011
- Format: Excel (`.xlsx`)
- Nature: Public sample dataset (UK-based online retail)

### Columns in Dataset

| Column Name   | Description |
|--------------|------------|
| InvoiceNo    | Transaction ID (starts with `C` for cancellations) |
| StockCode    | Product identifier |
| Description  | Product name |
| Quantity     | Quantity purchased |
| InvoiceDate  | Date and time of transaction |
| UnitPrice   | Price per unit |
| CustomerID  | Customer identifier |
| Country     | Customer country |

---

## 3. Tech Stack Used

- Python 3
- Pandas
- PostgreSQL
- Supabase (Cloud PostgreSQL)
- Looker Studio
- Git & GitHub

---

## 4. Project Structure

StarLinkProject/
│
├── data/
│ └── StarLinkRetail.xlsx
│
├── src/
│ ├── main.py
│ ├── data_loader.py
│ ├── data_cleaner.py
│ ├── db_loader.py
│ └── config.py
│
├── requirements.txt
├── .gitignore
└── README.md