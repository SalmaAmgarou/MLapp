import pandas as pd
import json

def load_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None

def load_excel(file_path):
    try:
        data = pd.read_excel(file_path)
        return data
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return None

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return None

def load_data(file_path):
    if file_path.endswith('.csv'):
        return load_csv(file_path)
    elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
        return load_excel(file_path)
    elif file_path.endswith('.json'):
        return load_json(file_path)
    else:
        print("Unsupported file format")
        return None
