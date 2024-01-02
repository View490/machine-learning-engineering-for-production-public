import json
import argparse

def gpt_print_nested_structure(data, depth=0, contents=None):
    if contents is None:
        contents = []

    if isinstance(data, dict):
        global key
        for key, value in data.items():
            gpt_print_nested_structure(value, depth + 1, contents)

    elif isinstance(data, list):
        for i, item in enumerate(data):
            gpt_print_nested_structure(item, depth, contents)

    elif (isinstance, str):       
        deepest_level = depth-1
        if key == 'detail':
            deepest_level = 0 
        deepest_content = "#" * deepest_level + " " + str(data)
        contents.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": [deepest_content]
        })

def gpt_json_to_ipynb(json_file_path, output_path):
    with open(json_file_path, 'r') as f:
        json_data = json.load(f)

    contents = []  # Ensure contents is initialized as an empty list
    gpt_print_nested_structure(json_data, contents=contents)

    with open(output_path, 'w') as f:
        notebook_content = {
            "cells": contents,
            "metadata": {}
        }

        # Write the Jupyter Notebook content to the file
        json.dump(notebook_content, f, indent=2)
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert JSON to Python notebook')
    parser.add_argument('json_file', type=str, help='Path to the JSON file')
    parser.add_argument('output_notebook', type=str, help='Path to the output Python notebook')
    args = parser.parse_args()
    
    gpt_json_to_ipynb(args.json_file, args.output_notebook)
