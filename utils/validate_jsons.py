import os
import json
import requests
from jsonschema import validate, RefResolver, ValidationError

def find_json_files(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.json'):
                yield os.path.join(dirpath, filename)

def load_schema(schema_path):
    if schema_path.startswith('http'):
        response = requests.get(schema_path)
        response.raise_for_status()
        return response.json()
    else:
        # Local schema file
        if not os.path.isabs(schema_path):
            # Resolve relative path from the JSON file's directory
            json_dir = os.path.dirname(json_path) if 'json_path' in locals() else "."
            schema_path = os.path.join(json_dir, schema_path)
        with open(schema_path, 'r', encoding='utf-8') as f:
            return json.load(f)

def main():
    root = "ReplET"
    all_valid = True
    for json_path in find_json_files(root):
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        schema_url = data.get('$schema')
        if not schema_url:
            print(f"[WARN] {json_path} não possui campo $schema.")
            continue
        try:
            # Resolve schema path relative to JSON file
            if not schema_url.startswith('http'):
                json_dir = os.path.dirname(json_path)
                schema_path = os.path.join(json_dir, schema_url)
            else:
                schema_path = schema_url
            
            schema = load_schema(schema_path)
            resolver = RefResolver(base_uri=schema_url, referrer=schema)
            validate(instance=data, schema=schema, resolver=resolver)
            print(f"[OK] {json_path} válido.")
        except ValidationError as e:
            print(f"[ERRO] {json_path} inválido: {e.message}")
            all_valid = False
        except Exception as e:
            print(f"[ERRO] {json_path} erro ao validar: {e}")
            all_valid = False
    if all_valid:
        print("Todos os arquivos JSON são válidos!")
    else:
        print("Alguns arquivos JSON não passaram na validação.")

if __name__ == "__main__":
    main() 