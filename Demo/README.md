# ReplET Demo - Complete Example Implementation

This `Demo/` directory provides a **complete, realistic example** of how to use the ReplET template for an eye tracking study in Software Engineering research.

## What This Demo Shows

This example demonstrates a realistic eye tracking study investigating:
- **Research Question**: How do different code complexity levels affect developer attention patterns?
- **Stimuli**: Two Python code snippets with varying complexity (S01: simple factorial, S02: complex editor interface)
- **Participants**: 5 fictional participants with realistic demographic data
- **Complete Data Pipeline**: From raw data collection to analysis results

## Demo Structure

This demo includes **all components** of a complete ReplET study:

### 📊 **Core Data Files**
- `metadata.json` - Study overview and basic information
- `participants/participants.json` - Demographic data for 5 participants
- `equipment/` - Hardware and software configuration
- `stimuli/` - Code stimuli with annotations and complexity metrics
- `aois/` - Areas of Interest definitions for both stimuli
- `collection/protocol.json` - Data collection procedures
- `preprocessing/` - Data cleaning and preprocessing steps
- `analysis/` - Statistical analysis configuration and results
- `validity/` - Validity threats and mitigation strategies
- `reproducibility/` - Complete reproducibility information

### 🔧 **Validation & Tools**
- `schemas/` - JSON schemas for all data formats (identical to main ReplET)
- `validate_jsons.py` - Validation script to check data integrity
- `repl_et_score.py` - Reproducibility scoring system
- `tests/` - Comprehensive test suite (35 tests)

### 📁 **Example Files**
- `stimuli/factorial.py` - Simple stimulus code
- `stimuli/editor.png` - Complex stimulus interface
- Realistic eye tracking data and analysis results

## How to Use This Demo

1. **Explore the Structure**: Browse through each directory to understand the ReplET format
2. **Validate the Data**: Run `python validate_jsons.py` to see validation in action
3. **Check Reproducibility**: Run `python repl_et_score.py` to see the scoring system (outputs to temporary directory)
4. **Run Tests**: Execute `pytest` to verify data integrity
5. **Adapt for Your Study**: Use this as a template for your own research

## Realistic Sample Data

All data in this demo is **realistic but fictional**:
- Eye tracking metrics match typical Software Engineering studies
- Participant demographics represent common developer populations  
- Code complexity measures use established metrics
- Statistical results follow expected patterns

## Purpose

This demo serves as:
- ✅ **Complete Example** of ReplET template usage
- ✅ **Reference Implementation** for new studies
- ✅ **Validation Test** for the ReplET system
- ✅ **Training Material** for researchers

**Start with this demo** to understand how ReplET works, then adapt it for your own eye tracking research in Software Engineering and HCI. 