"""
Cafe Sales Data Cleaning Script.

Objective:
This script reads a "dirty" CSV file, performs a complete data cleaning process,
and saves the result to a new, clean CSV file.

The cleaning process includes:
- Adjusting data types (numeric and datetime).
- Standardizing missing values (e.g., 'UNKNOWN', 'ERROR' to NaN).
- Removing rows with missing essential data.
- Filling contextual data (like 'Location') with the most frequent value (mode).
- Validating and recalculating the total spent column ('Total Spent').
- Checking for and removing duplicate rows.

How to use:
Run the script from the terminal, specifying the input and output files.

Example:
python clean_cafe_sales.py ../data/raw/dirty_cafe_sales.csv ../data/processed/cleaned_cafe_sales.csv
"""

import pandas as pd
import numpy as np
import argparse

def clean_data(input_file, output_file):
    """
    Main function that executes the entire data cleaning workflow.
    """
    # --- Introduction: Load the data ---
    try:
        df = pd.read_csv(input_file)
        print(f"File '{input_file}' loaded successfully!")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found!")
        return

    df_clean = df.copy()

    # --- Step 1: Adjusting Data Types ---
    print("Adjusting data types...")
    
    numeric_columns = ['Price Per Unit', 'Quantity', 'Total Spent']
    for column in numeric_columns:
        df_clean[column] = pd.to_numeric(df_clean[column], errors='coerce')

    df_clean['Transaction Date'] = pd.to_datetime(df_clean['Transaction Date'], errors='coerce')
    print("Data types adjusted.")

    # --- Step 2: Standardizing Errors ---
    print("Standardizing missing values and errors...")
    values_to_treat_as_null = ['', ' ', 'UNKNOWN', 'ERROR']
    df_clean.replace(values_to_treat_as_null, np.nan, inplace=True)
    print("Values standardized to NaN.")

    # --- Step 3: Correcting Errors and Handling Nulls ---
    print("Correcting errors and handling null values...")
    
    # Column classification
    essential_columns = ['Transaction Date', 'Price Per Unit', 'Quantity', 'Item']
    contextual_columns = ['Location', 'Payment Method']

    # Remove rows with nulls in essential columns
    initial_rows = len(df_clean)
    df_clean.dropna(subset=essential_columns, inplace=True)
    print(f"Removed {initial_rows - len(df_clean)} rows with missing essential data.")

    # Fill nulls in contextual columns with the mode
    for column in contextual_columns:
        mode = df_clean[column].mode()[0]
        df_clean[column] = df_clean[column].fillna(mode)
        print(f"Null values in '{column}' filled with the mode: '{mode}'.")

    # Validate and recalculate the 'Total Spent' column
    df_clean['Total Spent'] = df_clean['Quantity'] * df_clean['Price Per Unit']
    print("'Total Spent' column has been validated and recalculated.")

    # --- Step 4: Checking for and Removing Duplicates ---
    print("Checking for duplicate data...")
    num_duplicates = df_clean.duplicated().sum()
    if num_duplicates > 0:
        print(f"Found and removed {num_duplicates} duplicate rows.")
        df_clean.drop_duplicates(inplace=True)
    else:
        print("No duplicate rows found.")

    # --- Step 5: Final Validation and Saving ---
    print("\nCleaning process completed.")
    print(f"The clean DataFrame contains {len(df_clean)} rows.")
    
    # Save the new clean CSV file
    try:
        df_clean.to_csv(output_file, index=False, encoding='utf-8')
        print(f"Clean file saved successfully to: '{output_file}'")
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    # Setup argument parser
    parser = argparse.ArgumentParser(description="A script to clean cafe sales data.")
    
    parser.add_argument('input_file', 
                        type=str, 
                        help="Path to the input (dirty) CSV file.")
    
    parser.add_argument('output_file', 
                        type=str, 
                        help="Path to save the output (clean) CSV file.")

    args = parser.parse_args()

    # Call the main function with the provided arguments
    clean_data(args.input_file, args.output_file)