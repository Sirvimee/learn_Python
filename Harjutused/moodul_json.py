"""Loo funktsioon parse_json(json_text: str), mis võtab sisendina JSON-teksti ja tagastab selle Pythoni sõnastikuna."""

import json

def parse_json(json_text: str) -> dict:
    return json.loads(json_text)

json_text = '{"name": "John", "age": 30, "city": "New York"}'
parsed_data = parse_json(json_text)
print(parsed_data) # {'name': 'John', 'age': 30, 'city': 'New York'}