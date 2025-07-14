import os
import json
import pytest
import jsonschema
from jsonschema import validate, ValidationError

def load_json_file(file_path):
    """Load and return JSON file content."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_schema(schema_path):
    """Load schema file."""
    return load_json_file(schema_path)

class TestSchemas:
    """Test suite for JSON schema validation."""
    
    def test_metadata_schema_validity(self):
        """Test if metadata.schema.json is valid JSON Schema Draft 7."""
        schema = load_schema("schemas/metadata.schema.json")
        # This should not raise an exception
        jsonschema.Draft7Validator.check_schema(schema)
    
    def test_participants_schema_validity(self):
        """Test if participants.schema.json is valid JSON Schema Draft 7."""
        schema = load_schema("schemas/participants.schema.json")
        jsonschema.Draft7Validator.check_schema(schema)
    
    def test_all_schemas_are_valid(self):
        """Test that all schema files are valid JSON Schema Draft 7."""
        schema_files = [
            "schemas/metadata.schema.json",
            "schemas/participants.schema.json",
            "schemas/tracker_specs.schema.json",
            "schemas/screen_setup.schema.json",
            "schemas/software_env.schema.json",
            "schemas/stimuli_metadata.schema.json",
            "schemas/stimuli_annotations.schema.json",
            "schemas/aois_definition.schema.json",
            "schemas/protocol.schema.json",
            "schemas/preprocessing.schema.json",
            "schemas/analysis.schema.json",
            "schemas/validity.schema.json",
            "schemas/reproducibility.schema.json"
        ]
        
        for schema_file in schema_files:
            if os.path.exists(schema_file):
                schema = load_schema(schema_file)
                jsonschema.Draft7Validator.check_schema(schema)

class TestDataValidation:
    """Test suite for data file validation against schemas."""
    
    def test_metadata_against_schema(self):
        """Test metadata.json validates against its schema."""
        if os.path.exists("metadata.json"):
            data = load_json_file("metadata.json")
            schema = load_schema("schemas/metadata.schema.json")
            validate(instance=data, schema=schema)
    
    def test_participants_against_schema(self):
        """Test participants.json validates against its schema."""
        if os.path.exists("participants/participants.json"):
            data = load_json_file("participants/participants.json")
            schema = load_schema("schemas/participants.schema.json")
            validate(instance=data, schema=schema)
    
    def test_equipment_files_against_schemas(self):
        """Test equipment JSON files validate against their schemas."""
        equipment_files = [
            ("equipment/tracker_specs.json", "schemas/tracker_specs.schema.json"),
            ("equipment/screen_setup.json", "schemas/screen_setup.schema.json"),
            ("equipment/software_env.json", "schemas/software_env.schema.json")
        ]
        
        for data_file, schema_file in equipment_files:
            if os.path.exists(data_file):
                data = load_json_file(data_file)
                schema = load_schema(schema_file)
                validate(instance=data, schema=schema)
    
    def test_stimuli_files_against_schemas(self):
        """Test stimuli JSON files validate against their schemas."""
        stimuli_files = [
            ("stimuli/stimuli_metadata.json", "schemas/stimuli_metadata.schema.json"),
            ("stimuli/stimuli_annotations.json", "schemas/stimuli_annotations.schema.json")
        ]
        
        for data_file, schema_file in stimuli_files:
            if os.path.exists(data_file):
                data = load_json_file(data_file)
                schema = load_schema(schema_file)
                validate(instance=data, schema=schema)
    
    def test_all_json_files_validate(self):
        """Test all JSON files in the repository validate against their declared schemas."""
        json_files = []
        
        # Find all JSON files
        for root, dirs, files in os.walk("."):
            for file in files:
                if file.endswith(".json") and not file.endswith(".schema.json"):
                    json_files.append(os.path.join(root, file))
        
        for json_file in json_files:
            data = load_json_file(json_file)
            
            # Skip files that are arrays (not objects with $schema)
            if not isinstance(data, dict):
                continue
                
            schema_path = data.get("$schema")
            
            if schema_path and not schema_path.startswith("http"):
                # Resolve relative schema path
                json_dir = os.path.dirname(json_file)
                full_schema_path = os.path.join(json_dir, schema_path)
                
                if os.path.exists(full_schema_path):
                    schema = load_schema(full_schema_path)
                    validate(instance=data, schema=schema)

if __name__ == "__main__":
    pytest.main([__file__]) 