# Validity.schema Schema

Schema for validity.schema data

## Schema Structure

```json
{
    "title": "Repl.ET Validity Schema",
    "type": "object",
    "required": [
        "threats",
        "limitations"
    ],
    "properties": {
        "threats": {
            "type": "array",
            "items": {
                "type": "object",
                "required": [
                    "type",
                    "description"
                ],
                "properties": {
                    "type": {
                        "type": "string"
                    },
                    "description": {
                        "type": "string"
                    }
                }
            }
        },
        "limitations": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "confounding_factors": {
            "type": "array",
            "items": {
                "type": "string"
            }
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
with open('schemas/validity.schema.schema.json', 'r') as f:
    schema = json.load(f)
    
# Load and validate data
with open('validity.schema.json', 'r') as f:
    data = json.load(f)
    
jsonschema.validate(data, schema)
print('✅ Validation successful!')
"
```
