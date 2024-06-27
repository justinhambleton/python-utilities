import pandas as pd
import sys
import os

def csv_to_json(input_csv_file):
    # Check if the CSV file exists
    if not os.path.isfile(input_csv_file):
        print(f"Error: The file {input_csv_file} does not exist.")
        sys.exit(1)

    # Get the base name of the CSV file without extension
    base_name = os.path.basename(input_csv_file).rsplit('.', 1)[0]

    # Set the output JSON file path in the same directory as the input CSV file
    output_json_file = os.path.join(os.path.dirname(input_csv_file), f"{base_name}.json")

    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(input_csv_file)

    # Convert the DataFrame to a JSON file
    df.to_json(output_json_file, orient='records', lines=True)
    print(f"CSV file {input_csv_file} has been converted to JSON file {output_json_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python csv_to_json.py <input_csv_file>")
        sys.exit(1)

    input_csv_file = sys.argv[1]
    csv_to_json(input_csv_file)
