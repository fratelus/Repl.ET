# Aois_definition.schema Schema

Schema for aois_definition.schema data

## Schema Structure

```json
{
    "title": "Repl.ET AOIs Definition Schema",
    "type": "object",
    "required": [
        "aois",
        "aoi_strategy"
    ],
    "properties": {
        "aois": {
            "type": "array",
            "items": {
                "type": "object",
                "required": [
                    "aoi_id",
                    "stimulus_id",
                    "label",
                    "shape",
                    "coordinates"
                ],
                "properties": {
                    "aoi_id": {
                        "type": "string"
                    },
                    "stimulus_id": {
                        "type": "string"
                    },
                    "label": {
                        "type": "string"
                    },
                    "shape": {
                        "type": "string"
                    },
                    "coordinates": {
                        "type": "object",
                        "required": [
                            "x",
                            "y",
                            "width",
                            "height"
                        ],
                        "properties": {
                            "x": {
                                "type": "number"
                            },
                            "y": {
                                "type": "number"
                            },
                            "width": {
                                "type": "number",
                                "minimum": 0
                            },
                            "height": {
                                "type": "number",
                                "minimum": 0
                            }
                        }
                    }
                }
            }
        },
        "aoi_strategy": {
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
with open('schemas/aois_definition.schema.schema.json', 'r') as f:
    schema = json.load(f)
    
# Load and validate data
with open('aois_definition.schema.json', 'r') as f:
    data = json.load(f)
    
jsonschema.validate(data, schema)
print('✅ Validation successful!')
"
```
