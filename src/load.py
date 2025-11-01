from sqlalchemy import create_engine
import psycopg2
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

def load_to_db(file_name):
    db_host = os.getenv('host')
    db_name = os.getenv('database_name')
    db_pass = os.getenv('password')
    db_port = os.getenv('port')
    db_user = os.getenv('username')

    print(db_host)

    df = pd.read_csv('/Users/arthuruchebo_Pro/Documents/Projects/Amdari/amdari_DE/Prime_Square_Properties/data/transformed/San Antonio_TX_properties_data.csv')

    engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_pass}@{db_host}/{db_name}')

    df.to_sql('properties', engine, if_exists= 'replace')
    
    print("data successfully loaded to postgres")