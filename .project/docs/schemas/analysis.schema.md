# Analysis.schema Schema

Schema for analysis.schema data

## Schema Structure

```json
{
    "title": "Repl.ET Analysis Schema",
    "type": "object",
    "required": [
        "metrics",
        "statistical_methods",
        "software_used",
        "scripts"
    ],
    "properties": {
        "metrics": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "aoi_based_metrics": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "statistical_methods": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "dependent_variables": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "software_used": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "scripts": {
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
with open('schemas/analysis.schema.schema.json', 'r') as f:
    schema = json.load(f)
    
# Load and validate data
with open('analysis.schema.json', 'r') as f:
    data = json.load(f)
    
jsonschema.validate(data, schema)
print('✅ Validation successful!')
"
```
