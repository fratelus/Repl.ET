import os
import json
import pytest
import pandas as pd
from typing import Dict, List

def load_json_file(file_path):
    """Load and return JSON file content."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

class TestDataIntegrity:
    """Test suite for data integrity and cross-file consistency."""
    
    def test_stimulus_id_consistency(self):
        """Test that stimulus IDs are consistent across files."""
        if not (os.path.exists("stimuli/stimuli_metadata.json") and 
                os.path.exists("stimuli/stimuli_annotations.json") and
                os.path.exists("aois/aois_definition.json")):
            pytest.skip("Required stimulus files not found")
        
        # Get stimulus IDs from metadata
        metadata = load_json_file("stimuli/stimuli_metadata.json")
        metadata_ids = {s["stimulus_id"] for s in metadata["stimuli"]}
        
        # Get stimulus IDs from annotations
        annotations = load_json_file("stimuli/stimuli_annotations.json")
        annotation_ids = {a["stimulus_id"] for a in annotations["annotations"]}
        
        # Get stimulus IDs from AOIs
        aois = load_json_file("aois/aois_definition.json")
        aoi_ids = {a["stimulus_id"] for a in aois["aois"]}
        
        # Check consistency
        assert metadata_ids == annotation_ids, "Stimulus IDs mismatch between metadata and annotations"
        assert metadata_ids.issubset(aoi_ids), "Some stimuli missing AOI definitions"
    
    def test_participant_id_consistency(self):
        """Test that participant IDs are consistent across data files."""
        if not os.path.exists("participants/participants.json"):
            pytest.skip("Participants file not found")
        
        participants = load_json_file("participants/participants.json")
        participant_ids = {p["participant_id"] for p in participants["participants"]}
        
        # Check if results tables exist and validate participant IDs
        results_dir = "analysis/results_tables"
        if os.path.exists(results_dir):
            for file in os.listdir(results_dir):
                if file.endswith(".csv"):
                    csv_path = os.path.join(results_dir, file)
                    try:
                        df = pd.read_csv(csv_path)
                        if "participant_id" in df.columns:
                            csv_participant_ids = set(df["participant_id"].unique())
                            assert csv_participant_ids.issubset(participant_ids), \
                                f"Unknown participant IDs in {file}: {csv_participant_ids - participant_ids}"
                    except Exception as e:
                        # Skip files that can't be read as CSV
                        continue
    
    def test_aoi_coordinates_validity(self):
        """Test that AOI coordinates are valid (positive dimensions)."""
        if not os.path.exists("aois/aois_definition.json"):
            pytest.skip("AOIs file not found")
        
        aois = load_json_file("aois/aois_definition.json")
        
        for aoi in aois["aois"]:
            coords = aoi["coordinates"]
            assert coords["width"] > 0, f"AOI {aoi['aoi_id']} has invalid width"
            assert coords["height"] > 0, f"AOI {aoi['aoi_id']} has invalid height"
            assert coords["x"] >= 0, f"AOI {aoi['aoi_id']} has negative x coordinate"
            assert coords["y"] >= 0, f"AOI {aoi['aoi_id']} has negative y coordinate"
    
    def test_stimulus_files_exist(self):
        """Test that referenced stimulus files actually exist."""
        if not os.path.exists("stimuli/stimuli_metadata.json"):
            pytest.skip("Stimulus metadata file not found")
        
        metadata = load_json_file("stimuli/stimuli_metadata.json")
        stimuli_raw_dir = "stimuli/stimuli_raw"
        
        if not os.path.exists(stimuli_raw_dir):
            pytest.skip("Stimuli raw directory not found")
        
        for stimulus in metadata["stimuli"]:
            file_path = os.path.join(stimuli_raw_dir, stimulus["file_name"])
            assert os.path.exists(file_path), f"Stimulus file not found: {file_path}"
    
    def test_equipment_specs_consistency(self):
        """Test that equipment specifications are internally consistent."""
        equipment_files = [
            "equipment/tracker_specs.json",
            "equipment/screen_setup.json", 
            "equipment/software_env.json"
        ]
        
        for file_path in equipment_files:
            if os.path.exists(file_path):
                data = load_json_file(file_path)
                
                # Basic consistency checks
                if "sampling_rate_hz" in data:
                    assert data["sampling_rate_hz"] > 0, "Sampling rate must be positive"
                
                if "resolution_px" in data:
                    assert len(data["resolution_px"]) == 2, "Resolution must have width and height"
                    assert all(r > 0 for r in data["resolution_px"]), "Resolution values must be positive"
                
                if "distance_cm" in data:
                    assert data["distance_cm"] > 0, "Distance must be positive"
    
    def test_analysis_metrics_validity(self):
        """Test that analysis metrics are properly defined."""
        if not os.path.exists("analysis/analysis.json"):
            pytest.skip("Analysis file not found")
        
        analysis = load_json_file("analysis/analysis.json")
        
        # Check required fields
        assert "metrics" in analysis, "Metrics field required in analysis.json"
        assert "statistical_methods" in analysis, "Statistical methods field required"
        assert "software_used" in analysis, "Software used field required"
        
        # Check metrics are not empty
        assert len(analysis["metrics"]) > 0, "At least one metric must be defined"
        assert len(analysis["statistical_methods"]) > 0, "At least one statistical method must be defined"
    
    def test_preprocessing_pipeline_completeness(self):
        """Test that preprocessing pipeline is complete and logical."""
        if not os.path.exists("preprocessing/preprocessing.json"):
            pytest.skip("Preprocessing file not found")
        
        preprocessing = load_json_file("preprocessing/preprocessing.json")
        
        assert "steps" in preprocessing, "Steps field required in preprocessing.json"
        assert len(preprocessing["steps"]) > 0, "At least one preprocessing step required"
        
        # Check each step has required fields
        for step in preprocessing["steps"]:
            assert "step" in step, "Step name required"
            assert "method" in step, "Method required for each step"
            assert "parameters" in step, "Parameters required for each step"
    
    def test_validity_threats_completeness(self):
        """Test that validity threats are properly categorized."""
        if not os.path.exists("validity/validity.json"):
            pytest.skip("Validity file not found")
        
        validity = load_json_file("validity/validity.json")
        
        assert "threats" in validity, "Threats field required"
        assert "limitations" in validity, "Limitations field required"
        
        # Check threat types are valid
        valid_threat_types = ["internal", "external", "construct", "conclusion"]
        for threat in validity["threats"]:
            assert "type" in threat, "Threat type required"
            assert threat["type"] in valid_threat_types, f"Invalid threat type: {threat['type']}"
            assert "description" in threat, "Threat description required"

class TestFileStructure:
    """Test suite for repository file structure compliance."""
    
    def test_required_directories_exist(self):
        """Test that all required directories exist in project root."""
        required_dirs = [
            "schemas", "tests", "tools", "docs", "Demo", "Demo02"
        ]
        
        for directory in required_dirs:
            assert os.path.exists(directory), f"Required directory missing: {directory}"
    
    def test_demo_directories_exist(self):
        """Test that demo directories have required structure."""
        demo_dirs = ["Demo", "Demo02"]
        required_subdirs = [
            "participants", "equipment", "stimuli", "aois", 
            "collection", "preprocessing", "analysis", 
            "validity", "reproducibility"
        ]
        
        for demo_dir in demo_dirs:
            for subdir in required_subdirs:
                full_path = os.path.join(demo_dir, subdir)
                assert os.path.exists(full_path), f"Required demo directory missing: {full_path}"
    
    def test_required_files_exist(self):
        """Test that core required files exist."""
        required_files = [
            "README.md", "LICENSE", "metadata.json",
            "docs/repl_et_checklist.md", "config/requirements.txt"
        ]
        
        for file_path in required_files:
            assert os.path.exists(file_path), f"Required file missing: {file_path}"
    
    def test_schema_files_exist(self):
        """Test that all schema files exist."""
        expected_schemas = [
            "metadata.schema.json", "participants.schema.json",
            "tracker_specs.schema.json", "screen_setup.schema.json",
            "software_env.schema.json", "stimuli_metadata.schema.json",
            "stimuli_annotations.schema.json", "aois_definition.schema.json",
            "protocol.schema.json", "preprocessing.schema.json",
            "analysis.schema.json", "validity.schema.json",
            "reproducibility.schema.json"
        ]
        
        for schema_file in expected_schemas:
            schema_path = os.path.join("schemas", schema_file)
            assert os.path.exists(schema_path), f"Schema file missing: {schema_path}"

if __name__ == "__main__":
    pytest.main([__file__]) 