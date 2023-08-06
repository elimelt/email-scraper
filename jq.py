import json
import sys

def format_json(json_data):
    try:
        parsed_data = json.loads(json_data)
        formatted_data = json.dumps(parsed_data, indent=2)
        return formatted_data
    except json.JSONDecodeError as e:
        return f"Error: Invalid JSON - {e}"

if __name__ == "__main__":
    # Read JSON data from stdin (standard input)
    json_data = sys.stdin.read()
    formatted_json = format_json(json_data)
    print(formatted_json)

