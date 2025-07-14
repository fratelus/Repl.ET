# Stimuli_annotations.schema Schema

Schema for stimuli_annotations.schema data

## Schema Structure

```json
{
    "title": "Repl.ET Stimuli Annotations Schema",
    "type": "object",
    "required": [
        "annotations"
    ],
    "properties": {
        "annotations": {
            "type": "array",
            "items": {
                "type": "object",
                "required": [
                    "stimulus_id",
                    "ground_truth"
                ],
                "properties": {
                    "stimulus_id": {
                        "type": "string"
                    },
                    "ground_truth": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "required": [
                                "label"
                            ],
                            "properties": {
                                "line": {
                                    "type": "integer",
                                    "minimum": 1
                                },
                                "region": {
                                    "type": "string"
                                },
                                "label": {
                                    "type": "string"
                                }
                            },
                            "anyOf": [
                                {
                                    "required": [
                                        "line"
                                    ]
                                },
                                {
                                    "required": [
                                        "region"
                                    ]
                                }
                            ]
                        }
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
with open('schemas/stimuli_annotations.schema.schema.json', 'r') as f:
    schema = json.load(f)
    
# Load and validate data
with open('stimuli_annotations.schema.json', 'r') as f:
    data = json.load(f)
    
jsonschema.validate(data, schema)
print('✅ Validation successful!')
"
```
