# Tracker_specs.schema Schema

Schema for tracker_specs.schema data

## Schema Structure

```json
{
    "title": "Repl.ET Tracker Specs Schema",
    "type": "object",
    "required": [
        "manufacturer",
        "model",
        "sampling_rate_hz",
        "accuracy_deg",
        "firmware_version"
    ],
    "properties": {
        "manufacturer": {
            "type": "string"
        },
        "model": {
            "type": "string"
        },
        "sampling_rate_hz": {
            "type": "integer",
            "minimum": 1
        },
        "accuracy_deg": {
            "type": "number",
            "minimum": 0
        },
        "precision_rms_deg": {
            "type": "number",
            "minimum": 0
        },
        "firmware_version": {
            "type": "string"
        },
        "calibration_points": {
            "type": "integer",
            "minimum": 1
        },
        "tracking_area_cm": {
            "type": "array",
            "items": {
                "type": "number"
            }
        },
        "freedom_of_movement_cm": {
            "type": "array",
            "items": {
                "type": "number"
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
with open('schemas/tracker_specs.schema.schema.json', 'r') as f:
    schema = json.load(f)
    
# Load and validate data
with open('tracker_specs.schema.json', 'r') as f:
    data = json.load(f)
    
jsonschema.validate(data, schema)
print('✅ Validation successful!')
"
```
