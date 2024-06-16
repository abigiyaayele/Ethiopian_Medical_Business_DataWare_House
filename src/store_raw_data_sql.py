import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'port': '5432',
    'name': 'data_WareHouse',
    'user': 'postgres',
    'password': 'ocho'
}

# Create SQLAlchemy engine
db_url = f'postgresql://{db_config["user"]}:{db_config["password"]}@{db_config["host"]}:{db_config["port"]}/{db_config["name"]}'
engine = create_engine(db_url)

# Function to sanitize column names
def sanitize_column_names(df):
    df.columns = [col.replace('.', '_').replace(' ', '_') for col in df.columns]
    return df

# Function to load CSV to PostgreSQL
def load_csv_to_postgres(file, table_name):
    try:
        df = pd.read_csv(file)
        df = sanitize_column_names(df)
        df.to_sql(table_name, engine, if_exists='append', index=False)  # Use 'append' to add to existing table
        logger.info(f'Successfully stored data from {file} into table {table_name}')
    except Exception as e:
        logger.error(f'Error processing file {file}: {e}')

# Load each CSV file into the PostgreSQL database
csv_files = [
    '../telegram_data_scrapper/output/data/cheMed.csv',
    '../telegram_data_scrapper/output/data/Doctorset.csv',
    '../telegram_data_scrapper/output/data/EAHCI.csv',
    '../telegram_data_scrapper/output/data/lobelia4cosmetics.csv',
    '../telegram_data_scrapper/output/data/yetenaweg.csv',
    'imageoflobeli.csv',
]

for file in csv_files:
    table_name = file.split('.')[0]  # Use file name (without .csv) as table name
    load_csv_to_postgres(file, table_name)

# Execution
if __name__ == "__main__":
    # (The code is already set up for execution when run as a script)