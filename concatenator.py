import os
import pandas as pd
import sys

def concatenate_csv_files(input_dir):
    # Check if the input directory exists
    if not os.path.isdir(input_dir):
        print(f"Error: The directory {input_dir} does not exist.")
        sys.exit(1)

    # List all CSV files in the directory
    csv_files = [file for file in os.listdir(input_dir) if file.endswith('.csv')]

    if not csv_files:
        print(f"No CSV files found in the directory {input_dir}.")
        sys.exit(1)

    # Initialize an empty list to store dataframes
    df_list = []

    # Read and append each CSV file to the list
    for csv_file in csv_files:
        file_path = os.path.join(input_dir, csv_file)
        df = pd.read_csv(file_path)
        df_list.append(df)

    # Concatenate all dataframes
    concatenated_df = pd.concat(df_list, ignore_index=True)

    # Save the concatenated dataframe to a new CSV file
    output_file = os.path.join(input_dir, 'concatenated_output.csv')
    concatenated_df.to_csv(output_file, index=False)
    print(f"Concatenated CSV saved as {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python concatenate_csv_files.py <input_directory>")
        sys.exit(1)

    input_directory = sys.argv[1]
    concatenate_csv_files(input_directory)
