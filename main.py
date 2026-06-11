import os
from src.Postgres import Postgres
from src.util import get_file_headers

from dotenv import load_dotenv

# Loads variables in .env file into system
load_dotenv()

DATABASE_HOST = os.getenv('DATABASE_HOST')

TABLE_DDL = "CREATE TABLE IF NOT EXISTS data (acctnbr NUMERIC, memberagreenbr NUMERIC, rtxnnbr NUMERIC, tranamt NUMERIC, rtxntypcd TEXT, postdate DATE)"

postgres = Postgres(
    database = '',
    username = '',
    password = '',
    host = '',
)
connection = postgres.connect()

try:
    '''
        Insert file ingestion....
    '''
    
finally:
    connection.close()