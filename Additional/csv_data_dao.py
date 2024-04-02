"""
CVS Data DAO (Data Access Object).

This class provides methods to fetch data from an API, save it to a CSV file,
and export it to a SQL Server database.

Attributes:
- api_url: str, the URL of the API to fetch data from.

Methods:
- fetch_data_from_api(api_url): Fetches data from the specified API URL.
- save_to_csv(data, filename): Saves data to a CSV file with the given filename.
- export_to_sql_server(csv_filename, server, database, table): Exports data from a CSV file to a SQL Server database.

Dependencies:
- requests: Allows interaction with APIs.
- pyodbc: Provides Python DB API 2.0 interface for ODBC.
- csv: Provides functionality to read and write CSV files.

Returns:
None
        
Author: Serhii Spitsyn
"""

import requests
import pyodbc

class CVSDataDAO:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data_from_api(self, api_url):
        try:
            response = requests.get(api_url)
            response.raise_for_status() # Raise an exception for 4xx/5xx status codes
            return response.content
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {api_url}: {e}")
            return None
    
    def save_to_csv(self, data, filename):
        try:
            with open(filename, 'wb') as csv_file:
                csv_file.write(data)
            print(f"Data saved successfully to {filename}")
        except IOError as e:
            print(f"Error saving data to {filename}: {e}")
    
    def export_to_sql_server(self, csv_filename, server, database, table):
        try:
            conn = pyodbc.connect(f'Driver={{SQL Server}};Server={server};Database={database};Trusted_Connection=yes;')
            cursor = conn.cursor()

            # Open the CSV file and iterate over its rows to insert into the SQL Server table
            with open(csv_filename, 'r') as csv_file:
                csv_reader = csv_reader(csv_file)
                next(csv_reader)  # Skip the header row
                for row in csv_reader:
                    #TODO
                    cursor.execute(f"INSERT INTO {table} VALUES (?, ?, ?, ...)")
                
                conn.commit()
                print(f"Data exported to SQL Server table '{table}' successfully")
        except pyodbc.Error as e:
            print(f"Error exporting data to SQL Server: {e}")
        finally:
            if conn:
                conn.close()

