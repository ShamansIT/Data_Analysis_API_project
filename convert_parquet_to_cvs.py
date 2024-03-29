"""
Converts Parquet files to CSV files.

This script takes an input directory containing Parquet files and converts them to CSV format,
writing the resulting CSV files to the specified output directory.

Parameters:
- input_dir: str, the directory containing Parquet files.
- output_dir: str, the directory where the resulting CSV files will be saved.

Dependencies:
- path: a module providing paths to data directories.
- os: provides operating system interfaces.
- glob: provides a Unix style pathname pattern expansion.
- pandas (pd): provides data manipulation capabilities, including reading and writing Parquet files.

Returns:
None

Example:
parquet_to_csv(path.data_parquet, path.data_csv)

Author: Serhii Spitsyn
"""

import path
import os
import glob
import pandas as pd

def parquet_to_csv(input_dir, output_dir):
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate over all Parquet files in the input directory
    for parquet_file in glob.glob(os.path.join(input_dir, '**/*.parquet'), recursive=True):
        # Read Parquet file into a DataFrame
        df = pd.read_parquet(parquet_file)

        # Get relative path of Parquet file with respect to input directory
        relative_path = os.path.relpath(parquet_file, input_dir)

        # Construct output CSV file path
        csv_file = os.path.join(output_dir, os.path.splitext(relative_path)[0] + '.csv')

        # Ensure output directory structure exists
        csv_dir = os.path.dirname(csv_file)
        if not os.path.exists(csv_dir):
            os.makedirs(csv_dir)

        # Write DataFrame to CSV
        df.to_csv(csv_file, index=False)

        print(f"Converted {parquet_file} to {csv_file}")

parquet_to_csv(path.data_parquet, path.data_csv)
