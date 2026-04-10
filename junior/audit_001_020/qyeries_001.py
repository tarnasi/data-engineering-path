"""
This file need to do convert CSV file to PSQL data
"""
from pathlib import Path
import os
import pandas as pd
from sqlalchemy import create_engine

base_dir = Path.cwd().resolve()

connection_str = "postgresql+psycopg2://postgres:tarnasitarnasi@localhost:5444/novamart"

engine = create_engine(connection_str)


tables = {
    "customers": os.path.join('Brazilian_E_Commerce_DB', "olist_customers_dataset.csv"),
    "geolocation": os.path.join('Brazilian_E_Commerce_DB', "olist_geolocation_dataset.csv"),
    "order_items": os.path.join('Brazilian_E_Commerce_DB', "olist_order_items_dataset.csv"),
    "order_payments": os.path.join('Brazilian_E_Commerce_DB', "olist_order_payments_dataset.csv"),
    "order_reviews": os.path.join('Brazilian_E_Commerce_DB', "olist_order_reviews_dataset.csv"),
    "orders": os.path.join('Brazilian_E_Commerce_DB', "olist_orders_dataset.csv"),
    "products": os.path.join('Brazilian_E_Commerce_DB', "olist_products_dataset.csv"),
    "sellers": os.path.join('Brazilian_E_Commerce_DB', "olist_sellers_dataset.csv"),
    "p_category_translation": os.path.join('Brazilian_E_Commerce_DB', "product_category_name_translation.csv"),
}

def import_data_to_psql():
    for key, file in tables.items():
        print(f"Import {file} into table {key}")
        df = pd.read_csv(file)
        df.to_sql(key, con=engine, if_exists='replace', index=False)
        print(f"Success! Table '{key}' is ready.")

def main():
    sql = "select * from orders"
    df = pd.read_sql(sql, con=engine)
    print(df.columns)

if __name__ == "__main__":
    # import_data_to_psql()
    main()
