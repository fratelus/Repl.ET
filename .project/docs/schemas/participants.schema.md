# Participants.schema Schema

Schema for participants.schema data

## Schema Structure

```json
{
    "title": "Repl.ET Participants Schema",
    "type": "object",
    "required": [
        "participants",
        "inclusion_criteria"
    ],
    "properties": {
        "$schema": {
            "type": "string"
        },
        "participants": {
            "type": "array",
            "items": {
                "type": "object",
                "required": [
                    "participant_id",
                    "age",
                    "gender",
                    "handedness",
                    "vision",
                    "experience_years",
                    "programming_languages"
                ],
                "properties": {
                    "participant_id": {
                        "type": "string"
                    },
                    "age": {
                        "type": "integer",
                        "minimum": 0
                    },
                    "gender": {
                        "type": "string"
                    },
                    "handedness": {
                        "type": "string"
                    },
                    "vision": {
                        "type": "string"
                    },
                    "experience_years": {
                        "type": "integer",
                        "minimum": 0
                    },
                    "programming_languages": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "education": {
                        "type": "string"
                    },
                    "current_position": {
                        "type": "string"
                    }
                }
            }
        },
        "inclusion_criteria": {
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
with open('schemas/participants.schema.schema.json', 'r') as f:
    schema = json.load(f)
    
# Load and validate data
with open('participants.schema.json', 'r') as f:
    data = json.load(f)
    
jsonschema.validate(data, schema)
print('✅ Validation successful!')
"
```
