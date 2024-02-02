import json

__all__ = ['get_json_data', 'write_json_data']


def get_json_data(file_path: str) -> dict:
    with open(file_path, mode='r', encoding='UTF-8') as file:
        try:
            return json.load(file)
        except json.decoder.JSONDecodeError:
            print("File is empty or data type doesn't match JSON")
            return {}


def write_json_data(file_path: str, data: dict) -> None:
    with open(file_path, mode='w', encoding='UTF-8') as file:
        file.write(json.dumps(data))