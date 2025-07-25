# Software_env.schema Schema

Schema for software_env.schema data

## Schema Structure

```json
{
    "title": "Repl.ET Software Environment Schema",
    "type": "object",
    "required": [
        "os",
        "experiment_software",
        "tracker_driver_version",
        "python_version",
        "additional_packages"
    ],
    "properties": {
        "os": {
            "type": "string"
        },
        "experiment_software": {
            "type": "string"
        },
        "tracker_driver_version": {
            "type": "string"
        },
        "python_version": {
            "type": "string"
        },
        "additional_packages": {
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
with open('schemas/software_env.schema.schema.json', 'r') as f:
    schema = json.load(f)
    
# Load and validate data
with open('software_env.schema.json', 'r') as f:
    data = json.load(f)
    
jsonschema.validate(data, schema)
print('✅ Validation successful!')
"
```
