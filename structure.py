import json
import sys

def get_structure(json_data, field_structure, path=None):
    if path is None:
        path = []

    if isinstance(json_data, dict):
        for key in json_data.keys():
            current_path = path + [key]
            field_structure[".".join(current_path)] = True
            get_structure(json_data[key], field_structure, current_path)

    elif isinstance(json_data, list):
        for index, item in enumerate(json_data):
            current_path = path + [str(index)]
            get_structure(item, field_structure, current_path)

    return field_structure

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename.json>")
        return

    file_name = sys.argv[1]

    try:
        # Load the JSON data from the file
        with open(file_name, "r") as json_file:
            json_data = json.load(json_file)

        # Call the function to get the structure
        field_structure = get_structure(json_data, {})

        # Output the structure of the keys
        for field in sorted(field_structure.keys()):
            print(f"- {field}")

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from '{file_name}'.")

if __name__ == "__main__":
    main()

