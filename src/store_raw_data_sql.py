import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# PostgreSQL connection details
DATABASE = 'data_WareHouse'
USER = 'postgres'
PASSWORD = 'ocho'
HOST = 'localhost'
PORT = '5432'

# List of CSV files
csv_files = [
    'cheMed.csv',
    'Doctorset.csv',
    'EACHI.csv',
    'lobelia4cosmetics.csv',
    'yetenaweg.csv',
    'imageoflobeli.csv',
]

# Create SQLAlchemy engine
engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')

# Function to sanitize column names
def sanitize_column_names(df):
    df.columns = [col.replace('.', '_').replace(' ', '_') for col in df.columns]
    return df

# Function to load CSV to PostgreSQL
def load_csv_to_postgres(file, table_name):
    try:
        df = pd.read_csv(file)
        df = sanitize_column_names(df)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        logger.info(f'Successfully stored data from {file} into table {table_name}')
    except Exception as e:
        logger.error(f'Error processing file {file}: {e}')

# Load each CSV file into the PostgreSQL database
for file in csv_files:
    table_name = file.split('.')[0]  # Use file name (without .csv) as table name
    load_csv_to_postgres(file, table_name)
