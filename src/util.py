import csv
import pandas as pd

def count_rows(df: pd.DataFrame) -> int:
    '''Counts how many rows are in a given dataframe...'''
    ct = 0
    
    for _ in len(df):
        ct+=1 
        
    return ct


def get_file_headers(file_path: str) -> list[str]:
    with open(file_path, 'r') as openFile:
        reader = csv.reader(openFile)
        headers = next(reader)
        
    return headers
        