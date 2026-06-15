import os
from src.Postgres import Postgres
from src.util import get_file_headers

from dotenv import load_dotenv

# Loads variables in .env file into system
load_dotenv()

TABLE_DDL = "CREATE TABLE IF NOT EXISTS data (acctnbr NUMERIC, memberagreenbr NUMERIC, rtxnnbr NUMERIC, tranamt NUMERIC, rtxntypcd TEXT, postdate DATE)"