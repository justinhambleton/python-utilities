import os
import sys
import json
from glob import glob

def concatenate_json_files(input_dir):
    # Ensure the input directory exists
    if not os.path.isdir(input_dir):
        print(f"The directory {input_dir} does not exist.")
        return

    # Find all JSON files in the directory
    json_files = glob(os.path.join(input_dir, '*.json'))

    if not json_files:
        print(f"No JSON files found in the directory {input_dir}.")
        return

    # List to store data from all JSON files
    concatenated_data = []

    # Read and concatenate all JSON files
    for json_file in json_files:
        with open(json_file, 'r') as f:
            data = json.load(f)
            concatenated_data.append(data)

    # Output file path
    output_file = os.path.join(input_dir, 'concatenated.json')

    # Write concatenated data to the output file
    with open(output_file, 'w') as f:
        json.dump(concatenated_data, f, indent=4)

    print(f"Concatenated {len(json_files)} JSON files into {output_file}")

if __name__ == "__main__":
    # Ensure an argument is passed
    if len(sys.argv) != 2:
        print("Usage: python concatenate_json.py <input_directory>")
        sys.exit(1)

    # Input directory from command-line argument
    input_directory = sys.argv[1]

    # Concatenate JSON files in the specified directory
    concatenate_json_files(input_directory)
