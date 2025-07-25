# Metadata.schema Schema

Schema for metadata.schema data

## Schema Structure

```json
{
    "title": "Repl.ET Metadata Schema",
    "type": "object",
    "required": [
        "study_title",
        "study_objective",
        "paradigm",
        "task_description",
        "keywords",
        "authors",
        "date",
        "license"
    ],
    "properties": {
        "$schema": {
            "type": "string"
        },
        "study_title": {
            "type": "string"
        },
        "study_objective": {
            "type": "string"
        },
        "paradigm": {
            "type": "string"
        },
        "task_description": {
            "type": "string"
        },
        "keywords": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "authors": {
            "type": "array",
            "items": {
                "type": "object",
                "required": [
                    "name",
                    "orcid"
                ],
                "properties": {
                    "name": {
                        "type": "string"
                    },
                    "orcid": {
                        "type": "string"
                    }
                }
            }
        },
        "date": {
            "type": "string",
            "format": "date"
        },
        "license": {
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
with open('schemas/metadata.schema.schema.json', 'r') as f:
    schema = json.load(f)
    
# Load and validate data
with open('metadata.schema.json', 'r') as f:
    data = json.load(f)
    
jsonschema.validate(data, schema)
print('✅ Validation successful!')
"
```
