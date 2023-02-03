import pandas as pd
from utils.SQL import engine

TABLE_NAME = "sample"

# Read CSV
df = pd.read_csv('data/sample.csv')

# Make column small later
df.columns = df.columns.str.lower()

# Write into DB
df.to_sql(TABLE_NAME, con=engine, if_exists='append', index=False)
