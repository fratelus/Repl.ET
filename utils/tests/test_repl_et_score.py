import os
import json
import pytest
import tempfile
import shutil
from unittest.mock import patch, MagicMock

# Import the scoring functions
import sys
sys.path.append('..')
try:
    from repl_et_score import (
        check_metadata, check_participants, check_equipment,
        check_stimuli, check_aois, check_data_quality,
        check_preprocessing, check_analysis, check_threats,
        check_reproducibility
    )
except ImportError:
    pytest.skip("repl_et_score module not available", allow_module_level=True)

class TestReplETScore:
    """Test suite for Repl.ET scoring system."""
    
    def test_metadata_scoring_perfect(self, temp_repo):
        """Test metadata scoring with perfect data."""
        metadata = {
            "study_title": "Test Study",
            "paradigm": "Test Paradigm", 
            "task_description": "Test Description"
        }
        
        with open("ReplET/metadata.json", "w") as f:
            json.dump(metadata, f)
        
        score = check_metadata()
        assert score == 1.0
    
    def test_metadata_scoring_partial(self, temp_repo):
        """Test metadata scoring with partial data."""
        metadata = {
            "study_title": "Test Study"
        }
        
        with open("ReplET/metadata.json", "w") as f:
            json.dump(metadata, f)
        
        score = check_metadata()
        assert 0.0 < score < 1.0
    
    def test_metadata_scoring_missing(self, temp_repo):
        """Test metadata scoring with missing file."""
        score = check_metadata()
        assert score == 0.0
    
    def test_participants_scoring_complete(self, temp_repo):
        """Test participants scoring with complete data."""
        participants = {
            "participants": [
                {
                    "participant_id": "P01",
                    "age": 25,
                    "gender": "female",
                    "handedness": "right",
                    "vision": "normal",
                    "experience_years": 3,
                    "programming_languages": ["Python"]
                }
            ]
        }
        
        with open("ReplET/participants/participants.json", "w") as f:
            json.dump(participants, f)
        
        score = check_participants()
        assert score == 1.0
    
    def test_equipment_scoring_all_files(self, temp_repo):
        """Test equipment scoring with all files present."""
        files = [
            "ReplET/equipment/tracker_specs.json",
            "ReplET/equipment/screen_setup.json", 
            "ReplET/equipment/software_env.json"
        ]
        
        for file_path in files:
            with open(file_path, "w") as f:
                json.dump({"test": "data"}, f)
        
        score = check_equipment()
        assert score == 1.0
    
    def test_equipment_scoring_partial_files(self, temp_repo):
        """Test equipment scoring with some files missing."""
        with open("ReplET/equipment/tracker_specs.json", "w") as f:
            json.dump({"test": "data"}, f)
        
        score = check_equipment()
        assert 0.0 < score < 1.0
    
    def test_stimuli_scoring_complete(self, temp_repo):
        """Test stimuli scoring with complete data."""
        # Create metadata file
        with open("ReplET/stimuli/stimuli_metadata.json", "w") as f:
            json.dump({"test": "data"}, f)
        
        # Create annotations file
        with open("ReplET/stimuli/stimuli_annotations.json", "w") as f:
            json.dump({"test": "data"}, f)
        
        # Create raw stimulus file
        with open("ReplET/stimuli/stimuli_raw/test.txt", "w") as f:
            f.write("test stimulus")
        
        score = check_stimuli()
        assert score == 1.0
    
    def test_aois_scoring_with_visualizations(self, temp_repo):
        """Test AOIs scoring with visualizations."""
        # Create AOIs definition
        with open("ReplET/aois/aois_definition.json", "w") as f:
            json.dump({"test": "data"}, f)
        
        # Create visualization file
        with open("ReplET/aois/aois_visualizations/test.png", "w") as f:
            f.write("fake image data")
        
        score = check_aois()
        assert score == 1.0
    
    def test_data_quality_scoring_complete(self, temp_repo):
        """Test data quality scoring with protocol and logs."""
        # Create protocol file
        with open("ReplET/collection/protocol.json", "w") as f:
            json.dump({"test": "data"}, f)
        
        # Create log file
        with open("ReplET/collection/logs/test.log", "w") as f:
            f.write("test log data")
        
        score = check_data_quality()
        assert score == 1.0
    
    def test_preprocessing_scoring_complete(self, temp_repo):
        """Test preprocessing scoring with JSON and scripts."""
        # Create preprocessing file
        with open("ReplET/preprocessing/preprocessing.json", "w") as f:
            json.dump({"test": "data"}, f)
        
        # Create script file
        with open("ReplET/preprocessing/scripts/test.py", "w") as f:
            f.write("# test script")
        
        score = check_preprocessing()
        assert score == 1.0
    
    def test_analysis_scoring_complete(self, temp_repo):
        """Test analysis scoring with all components."""
        # Create analysis file
        with open("ReplET/analysis/analysis.json", "w") as f:
            json.dump({"test": "data"}, f)
        
        # Create results table
        with open("ReplET/analysis/results_tables/test.csv", "w") as f:
            f.write("test,data\n1,2\n")
        
        # Create visualization
        with open("ReplET/analysis/visualizations/test.png", "w") as f:
            f.write("fake image")
        
        score = check_analysis()
        assert score == 1.0
    
    def test_threats_scoring_complete(self, temp_repo):
        """Test threats scoring with complete validity data."""
        validity = {
            "threats": [
                {"type": "internal", "description": "test threat"}
            ]
        }
        
        with open("ReplET/validity/validity.json", "w") as f:
            json.dump(validity, f)
        
        score = check_threats()
        assert score == 1.0
    
    def test_reproducibility_scoring_complete(self, temp_repo):
        """Test reproducibility scoring with all files."""
        files = [
            "ReplET/README.md",
            "ReplET/LICENSE", 
            "ReplET/reproducibility/environment.yml",
            "ReplET/reproducibility/CITATION.cff",
            "ReplET/repl_et_checklist.md"
        ]
        
        for file_path in files:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, "w") as f:
                f.write("test content")
        
        score = check_reproducibility()
        assert score == 1.0
    
    def test_score_bounds(self, temp_repo):
        """Test that all scoring functions return values between 0 and 1."""
        scoring_functions = [
            check_metadata, check_participants, check_equipment,
            check_stimuli, check_aois, check_data_quality,
            check_preprocessing, check_analysis, check_threats,
            check_reproducibility
        ]
        
        for func in scoring_functions:
            score = func()
            assert 0.0 <= score <= 1.0, f"Score out of bounds for {func.__name__}: {score}"

class TestScoreIntegration:
    """Integration tests for the complete scoring system."""
    
    @patch('matplotlib.pyplot.savefig')
    @patch('matplotlib.pyplot.subplots')
    def test_main_function_execution(self, mock_subplots, mock_savefig, temp_repo):
        """Test that main scoring function executes without errors."""
        # Mock matplotlib components
        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_subplots.return_value = (mock_fig, mock_ax)
        
        # Create minimal required structure
        os.makedirs("ReplET", exist_ok=True)
        
        # Import and run main (if available)
        try:
            from repl_et_score import main
            main()
            
            # Check that output files would be created
            assert mock_savefig.called
        except ImportError:
            pytest.skip("Main function not available")
    
    def test_score_consistency(self, temp_repo):
        """Test that scoring is consistent across multiple runs."""
        # Create some test data
        with open("ReplET/metadata.json", "w") as f:
            json.dump({"study_title": "Test", "paradigm": "Test"}, f)
        
        # Run scoring multiple times
        scores1 = [check_metadata() for _ in range(3)]
        scores2 = [check_metadata() for _ in range(3)]
        
        # Scores should be consistent
        assert scores1 == scores2

if __name__ == "__main__":
    pytest.main([__file__]) 