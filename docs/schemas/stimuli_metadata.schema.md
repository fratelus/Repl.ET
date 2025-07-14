# Stimuli_metadata.schema Schema

Schema for stimuli_metadata.schema data

## Schema Structure

```json
{
    "title": "Repl.ET Stimuli Metadata Schema",
    "type": "object",
    "required": [
        "stimuli"
    ],
    "properties": {
        "stimuli": {
            "type": "array",
            "items": {
                "type": "object",
                "required": [
                    "stimulus_id",
                    "type",
                    "description",
                    "file_name"
                ],
                "properties": {
                    "stimulus_id": {
                        "type": "string"
                    },
                    "type": {
                        "type": "string"
                    },
                    "description": {
                        "type": "string"
                    },
                    "file_name": {
                        "type": "string"
                    },
                    "lines_of_code": {
                        "type": "integer",
                        "minimum": 0
                    },
                    "complexity": {
                        "type": "string"
                    },
                    "bug_type": {
                        "type": "string"
                    },
                    "task_type": {
                        "type": "string"
                    }
                }
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
with open('schemas/stimuli_metadata.schema.schema.json', 'r') as f:
    schema = json.load(f)
    
# Load and validate data
with open('stimuli_metadata.schema.json', 'r') as f:
    data = json.load(f)
    
jsonschema.validate(data, schema)
print('✅ Validation successful!')
"
```
