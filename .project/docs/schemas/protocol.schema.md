# Protocol.schema Schema

Schema for protocol.schema data

## Schema Structure

```json
{
    "title": "Repl.ET Protocol Schema",
    "type": "object",
    "required": [
        "calibration",
        "drift_check",
        "exclusion_criteria",
        "instructions_to_participants"
    ],
    "properties": {
        "calibration": {
            "type": "object",
            "required": [
                "type",
                "criteria"
            ],
            "properties": {
                "type": {
                    "type": "string"
                },
                "criteria": {
                    "type": "string"
                },
                "recalibration_threshold": {
                    "type": "string"
                },
                "validation_points": {
                    "type": "integer",
                    "minimum": 1
                }
            }
        },
        "drift_check": {
            "type": "object",
            "required": [
                "interval_minutes",
                "criteria"
            ],
            "properties": {
                "interval_minutes": {
                    "type": "integer",
                    "minimum": 1
                },
                "criteria": {
                    "type": "string"
                },
                "correction_procedure": {
                    "type": "string"
                }
            }
        },
        "exclusion_criteria": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "session_structure": {
            "type": "object",
            "properties": {
                "practice_trials": {
                    "type": "integer",
                    "minimum": 0
                },
                "main_trials": {
                    "type": "integer",
                    "minimum": 1
                },
                "break_intervals": {
                    "type": "string"
                }
            }
        },
        "instructions_to_participants": {
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
with open('schemas/protocol.schema.schema.json', 'r') as f:
    schema = json.load(f)
    
# Load and validate data
with open('protocol.schema.json', 'r') as f:
    data = json.load(f)
    
jsonschema.validate(data, schema)
print('✅ Validation successful!')
"
```
