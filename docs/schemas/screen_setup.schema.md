# Screen_setup.schema Schema

Schema for screen_setup.schema data

## Schema Structure

```json
{
    "title": "Repl.ET Screen Setup Schema",
    "type": "object",
    "required": [
        "screen_size_inch",
        "resolution_px",
        "refresh_rate_hz",
        "distance_cm",
        "background_color"
    ],
    "properties": {
        "screen_size_inch": {
            "type": "number",
            "minimum": 1
        },
        "resolution_px": {
            "type": "array",
            "items": {
                "type": "integer",
                "minimum": 1
            },
            "minItems": 2,
            "maxItems": 2
        },
        "refresh_rate_hz": {
            "type": "integer",
            "minimum": 1
        },
        "distance_cm": {
            "type": "number",
            "minimum": 1
        },
        "background_color": {
            "type": "string"
        },
        "pixel_pitch_mm": {
            "type": "number",
            "minimum": 0
        },
        "brightness_cd_m2": {
            "type": "number",
            "minimum": 0
        },
        "contrast_ratio": {
            "type": "string"
        },
        "viewing_angle_deg": {
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
with open('schemas/screen_setup.schema.schema.json', 'r') as f:
    schema = json.load(f)
    
# Load and validate data
with open('screen_setup.schema.json', 'r') as f:
    data = json.load(f)
    
jsonschema.validate(data, schema)
print('✅ Validation successful!')
"
```
