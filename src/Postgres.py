from typing import Any
from io import TextIOWrapper

import psycopg2
from pydantic import BaseModel
from psycopg2.extensions import connection

class Postgres(BaseModel):
    """Lightweight PostgreSQL client that may be used during the interview exercise.
    
    This class abstracts common database operations such as executing SQL statements and loading data.
    """
    username: str
    password: str
    host: str
    database: str = None
    port: int = 5432
    
    def connect(self) -> connection:
        '''Connects to a postgres database and returns the connection object'''
        connection = psycopg2.connect(user = self.username,
                                      password = self.password,
                                      host = self.host,
                                      database = self.database,
                                      port = self.port
                                      )
        
        return connection
    
    def get_connection_string(self) -> str:
        ''' Builds a connection query that can be used for '''
        return f'postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}'

    def run_query(self, query: str, connection: connection) -> None:
        '''Takes a query and runs it in the connected database. DOES not return anything. Sets autocommit = True to remove transaction block, which will allow DDL type queries'''
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(query)
        print('Successfully ran query...')
        
    def get_data(self, query: str, connection: connection) -> tuple[Any]:
        '''Takes a query and runs it in the connected database. Returns the data as a tuple'''
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
            
    def load_csv(self,
                 csv_file_path: str,
                 table_name: str,
                 schema_name: str,
                 all_columns: list[str],
                 connection: connection
                 ) -> None: 
        '''Loads a csv into postgres
        
        Example:
            DATABASE_HOST = os.getenv('DATABASE_HOST')
            DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
            DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
            DATABASE = os.getenv('DATABASE')

            postgres = Postgres(
                database = DATABASE,
                username = DATABASE_USERNAME,
                password = DATABASE_PASSWORD,
                host = DATABASE_HOST,
            )

            connection = postgres.connect()
        
            postgres.load_csv(
                './random_csv.csv',
                'table_name',
                'schema_name',
                file_header_list,
                connection
            )
        
        '''
        copy_sql = f'''COPY {schema_name}.{table_name} ({",".join(column for column in all_columns)}) FROM stdin with csv header delimiter as ',' '''
        cursor = connection.cursor()
        
        with open(csv_file_path, 'r') as openFile:    
            cursor.copy_expert(copy_sql, openFile)
        
        connection.commit()
        print('Successfully loaded csv...')