# StarLink Retail Data Pipeline

This project demonstrates an end-to-end data pipeline:
Excel → Python → PostgreSQL (Supabase) → Looker Studio

## Tech Stack
- Python
- Pandas
- PostgreSQL
- Supabase
- Looker Studio

## Pipeline Flow
1. Load Excel retail data
2. Clean invalid records
3. Drop & recreate PostgreSQL table
4. Insert cleaned data
5. Visualize in Looker Studio

## How to Run
```bash
pip install -r requirements.txt
python src/main.py
