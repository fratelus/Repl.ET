# ✅ Validation API

## validate_jsons.py

Validates all JSON files against their corresponding schemas.

### Usage

```bash
python tools/validate_jsons.py
```

### Output

- ✅ Success: "Todos os arquivos JSON são válidos!"
- ❌ Error: Detailed validation error messages

### Example

```python
# Programmatic usage
import subprocess
import sys

result = subprocess.run(['python', 'validate_jsons.py'], 
                       capture_output=True, text=True)

if result.returncode == 0:
    print("✅ All validations passed")
else:
    print(f"❌ Validation failed: {result.stderr}")
```
