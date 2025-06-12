import pytest
import tempfile
import shutil
import os
import json

@pytest.fixture
def temp_repo():
    """Create a temporary repository structure for testing."""
    temp_dir = tempfile.mkdtemp()
    original_dir = os.getcwd()
    os.chdir(temp_dir)
    
    # Create basic structure
    os.makedirs("ReplET/participants", exist_ok=True)
    os.makedirs("ReplET/equipment", exist_ok=True)
    os.makedirs("ReplET/stimuli/stimuli_raw", exist_ok=True)
    os.makedirs("ReplET/aois/aois_visualizations", exist_ok=True)
    os.makedirs("ReplET/collection/logs", exist_ok=True)
    os.makedirs("ReplET/preprocessing/scripts", exist_ok=True)
    os.makedirs("ReplET/analysis/results_tables", exist_ok=True)
    os.makedirs("ReplET/analysis/visualizations", exist_ok=True)
    os.makedirs("ReplET/validity", exist_ok=True)
    os.makedirs("ReplET/reproducibility", exist_ok=True)
    
    yield temp_dir
    
    # Cleanup
    os.chdir(original_dir)
    shutil.rmtree(temp_dir)

@pytest.fixture
def sample_metadata():
    """Sample metadata for testing."""
    return {
        "$schema": "schemas/metadata.schema.json",
        "study_title": "Test Eye Tracking Study",
        "study_objective": "Test objective",
        "paradigm": "test_paradigm",
        "task_description": "Test task description",
        "keywords": ["eye tracking", "test"],
        "authors": [
            {"name": "Test Author", "orcid": "0000-0000-0000-0000"}
        ],
        "date": "2024-01-01",
        "license": "CC-BY-4.0"
    }

@pytest.fixture
def sample_participants():
    """Sample participants data for testing."""
    return {
        "$schema": "../schemas/participants.schema.json",
        "participants": [
            {
                "participant_id": "P01",
                "age": 25,
                "gender": "female",
                "handedness": "right",
                "vision": "normal",
                "experience_years": 3,
                "programming_languages": ["Python", "Java"]
            }
        ],
        "inclusion_criteria": "Test criteria"
    }

@pytest.fixture
def sample_stimuli_metadata():
    """Sample stimuli metadata for testing."""
    return {
        "$schema": "../schemas/stimuli_metadata.schema.json",
        "stimuli": [
            {
                "stimulus_id": "S01",
                "type": "code",
                "description": "Test code snippet",
                "file_name": "test.py"
            }
        ]
    }

@pytest.fixture
def sample_aois():
    """Sample AOIs data for testing."""
    return {
        "$schema": "../schemas/aois_definition.schema.json",
        "aois": [
            {
                "aoi_id": "A01",
                "stimulus_id": "S01",
                "label": "test_region",
                "shape": "rectangle",
                "coordinates": {"x": 10, "y": 20, "width": 100, "height": 50}
            }
        ],
        "aoi_strategy": "Test strategy"
    }

@pytest.fixture
def temp_repo_structure():
    """Create a temporary repository structure with all required directories."""
    temp_dir = tempfile.mkdtemp()
    original_dir = os.getcwd()
    os.chdir(temp_dir)
    
    # Create all required directories
    directories = [
        "participants", "equipment", "stimuli/stimuli_raw", 
        "aois/aois_visualizations", "collection/logs",
        "preprocessing/scripts", "analysis/results_tables",
        "analysis/visualizations", "validity", 
        "reproducibility", "schemas", "tests"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    
    yield temp_dir
    
    # Cleanup
    os.chdir(original_dir)
    shutil.rmtree(temp_dir)

@pytest.fixture
def populated_repo(temp_repo_structure, sample_metadata, sample_participants, 
                  sample_stimuli_metadata, sample_aois):
    """Create a repository structure populated with sample data."""
    
    # Write sample data files
    with open("metadata.json", "w") as f:
        json.dump(sample_metadata, f, indent=2)
    
    with open("participants/participants.json", "w") as f:
        json.dump(sample_participants, f, indent=2)
    
    with open("stimuli/stimuli_metadata.json", "w") as f:
        json.dump(sample_stimuli_metadata, f, indent=2)
    
    with open("aois/aois_definition.json", "w") as f:
        json.dump(sample_aois, f, indent=2)
    
    # Create some basic required files
    with open("README.md", "w") as f:
        f.write("# Test Repository")
    
    with open("LICENSE", "w") as f:
        f.write("Test License")
    
    with open("requirements.txt", "w") as f:
        f.write("pytest>=6.0.0\njsonschema>=4.0.0\n")
    
    # Create a sample stimulus file
    with open("stimuli/stimuli_raw/test.py", "w") as f:
        f.write("# Test code\nprint('hello world')")
    
    return temp_repo_structure

def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (may take several seconds)"
    )
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests"
    )
    config.addinivalue_line(
        "markers", "unit: marks tests as unit tests"
    )

def pytest_collection_modifyitems(config, items):
    """Automatically mark tests based on their names."""
    for item in items:
        # Mark integration tests
        if "integration" in item.nodeid or "test_main" in item.nodeid:
            item.add_marker(pytest.mark.integration)
        # Mark slow tests
        elif "slow" in item.nodeid or "test_all_" in item.nodeid:
            item.add_marker(pytest.mark.slow)
        # Mark unit tests
        else:
            item.add_marker(pytest.mark.unit) 