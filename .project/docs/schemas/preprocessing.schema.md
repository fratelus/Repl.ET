# Preprocessing.schema Schema

Schema for preprocessing.schema data

## Schema Structure

```json
{
    "title": "Repl.ET Preprocessing Schema",
    "type": "object",
    "required": [
        "steps",
        "software_used"
    ],
    "properties": {
        "steps": {
            "type": "array",
            "items": {
                "type": "object",
                "required": [
                    "step",
                    "method",
                    "parameters"
                ],
                "properties": {
                    "step": {
                        "type": "string"
                    },
                    "method": {
                        "type": "string"
                    },
                    "parameters": {
                        "type": "object"
                    }
                }
            }
        },
        "software_used": {
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
with open('schemas/preprocessing.schema.schema.json', 'r') as f:
    schema = json.load(f)
    
# Load and validate data
with open('preprocessing.schema.json', 'r') as f:
    data = json.load(f)
    
jsonschema.validate(data, schema)
print('✅ Validation successful!')
"
```
