# Reproducibility.schema Schema

Schema for reproducibility.schema data

## Schema Structure

```json
{
    "title": "Repl.ET Reproducibility Schema",
    "type": "object",
    "required": [
        "data_availability",
        "code_availability",
        "environment",
        "replication_instructions",
        "doi"
    ],
    "properties": {
        "data_availability": {
            "type": "string"
        },
        "code_availability": {
            "type": "string"
        },
        "environment": {
            "type": "string"
        },
        "replication_instructions": {
            "type": "string"
        },
        "doi": {
            "type": "string"
        },
        "$schema": {
            "type": "string"
        }
    },
    "additionalProperties": false
}
```

## Usage Example

```bash
# Validate against this schema
python -c "
import json
import jsonschema

# Load schema
with open('schemas/reproducibility.schema.schema.json', 'r') as f:
    schema = json.load(f)
    
# Load and validate data
with open('reproducibility.schema.json', 'r') as f:
    data = json.load(f)
    
jsonschema.validate(data, schema)
print('✅ Validation successful!')
"
```
