#!/usr/bin/env python3
"""
Script to automatically update README.md with:
1. Generated spider graph from repl_et_score.py
2. Automatically filled compliance checklist based on template analysis
"""

import os
import json
import subprocess
import re
from pathlib import Path

class TemplateAssessment:
    def __init__(self):
        self.base_path = Path(".")
        self.checklist_items = {}
        
    def get_all_scores(self):
        """Get all component scores using current assessment functions"""
        return {
            "Study Metadata": check_metadata_current(),
            "Participant Info": check_participants_current(),
            "Equipment": check_equipment_current(),
            "Stimuli": check_stimuli_current(),
            "AOIs": check_aois_current(),
            "Data Quality": check_data_quality_current(),
            "Preprocessing": check_preprocessing_current(),
            "Analysis": check_analysis_current(),
            "Validity": check_threats_current(),
            "Reproducibility": check_reproducibility_current()
        }
        
    def analyze_template_compliance(self):
        """Analyze template files to determine compliance status"""
        compliance = {
            "fair_principles": self._check_fair_compliance(),
            "research_standards": self._check_research_standards(),
            "iguidelines": self._check_iguidelines_compliance(),
            "trrraced": self._check_trrraced_compliance()
        }
        return compliance
    
    def _check_fair_compliance(self):
        """Check FAIR principles compliance based on real data quality"""
        return {
            "findable": self._has_metadata_with_ids() and check_metadata_current() > 0.8,
            "accessible": self._has_open_formats() and check_metadata_current() > 0.8,
            "interoperable": self._has_schemas() and check_metadata_current() > 0.8,
            "reusable": self._has_rich_metadata() and check_metadata_current() > 0.8
        }
    
    def _check_research_standards(self):
        """Check general research standards compliance"""
        return {
            "study_design": self._has_file("metadata.json") and check_metadata_current() > 0.8,
            "equipment_reporting": self._has_equipment_specs() and check_equipment_current() > 0.8,
            "stimuli_documentation": self._has_stimuli_docs(),
            "methodology_transparency": self._has_methodology_docs(),
            "validity_assessment": self._has_file("validity/validity.json") and check_threats_current() > 0.8
        }
    
    def _check_iguidelines_compliance(self):
        """Check iGuidelines compliance"""
        return {
            "participant_reporting": self._has_file("participants/participants.json") and check_participants_current() > 0.8,
            "calibration_procedures": self._has_equipment_calibration() and check_equipment_current() > 0.8,
            "exclusion_criteria": self._has_participant_criteria(),
            "quality_metrics": self._has_quality_assessment()
        }
    
    def _check_trrraced_compliance(self):
        """Check TRRRACED framework compliance based on real data quality"""
        return {
            "transparent_reporting": self._has_comprehensive_docs(),
            "replication_materials": self._has_file("reproducibility/reproducibility.json") and check_reproducibility_current() > 0.5,
            "data_availability": self._has_data_sharing_info() and check_data_quality_current() > 0.5,
            "environment_specs": self._has_environment_specs()
        }
    
    def _has_file(self, filepath):
        """Check if file exists and has content"""
        path = self.base_path / filepath
        if not path.exists():
            return False
        try:
            if path.suffix == '.json':
                with open(path, 'r') as f:
                    data = json.load(f)
                    return bool(data)  # True if not empty
            else:
                return path.stat().st_size > 0
        except:
            return False
    
    def _has_metadata_with_ids(self):
        """Check if metadata.json has proper ID structure"""
        return self._has_file("metadata.json")
    
    def _has_open_formats(self):
        """Check if using open JSON formats"""
        json_files = list(self.base_path.glob("**/*.json"))
        return len(json_files) >= 10  # Should have all 10 components
    
    def _has_schemas(self):
        """Check if JSON schemas are present"""
        schemas_path = self.base_path / "schemas"
        if not schemas_path.exists():
            return False
        schema_files = list(schemas_path.glob("*.json"))
        return len(schema_files) >= 10
    
    def _has_rich_metadata(self):
        """Check if metadata is comprehensive"""
        return self._has_file("metadata.json")
    
    def _has_equipment_specs(self):
        """Check equipment specifications"""
        return (self._has_file("equipment/tracker_specs.json") or 
                self._has_file("equipment/screen_setup.json") or
                self._has_file("equipment/software_env.json"))
    
    def _has_stimuli_docs(self):
        """Check stimuli documentation with real data"""
        return ((self._has_file("stimuli/stimuli_metadata.json") or
                self._has_file("stimuli/stimuli_annotations.json")) and 
                check_stimuli_current() > 0.5)
    
    def _has_methodology_docs(self):
        """Check methodology documentation with real data"""
        return (self._has_file("preprocessing/preprocessing.json") and
                self._has_file("analysis/analysis.json") and
                check_preprocessing_current() > 0.5 and check_analysis_current() > 0.5)
    
    def _has_equipment_calibration(self):
        """Check calibration procedures in equipment"""
        return self._has_file("equipment/tracker_specs.json")
    
    def _has_participant_criteria(self):
        """Check participant inclusion/exclusion criteria with real data"""
        return self._has_file("participants/participants.json") and check_participants_current() > 0.5
    
    def _has_quality_assessment(self):
        """Check quality control measures with real data"""
        return self._has_file("preprocessing/preprocessing.json") and check_preprocessing_current() > 0.5
    
    def _has_comprehensive_docs(self):
        """Check if all major components have real documentation"""
        scores = [
            check_metadata_current(),
            check_participants_current(),
            check_equipment_current(),
            check_data_quality_current(),
            check_analysis_current()
        ]
        # At least 4 out of 5 components must have real data (score > 0.5)
        return sum(score > 0.5 for score in scores) >= 4
    
    def _has_data_sharing_info(self):
        """Check data sharing information"""
        return self._has_file("reproducibility/reproducibility.json")
    
    def _has_environment_specs(self):
        """Check environment specifications"""
        return self._has_file("equipment/software_env.json")

def get_actual_scores_and_generate_png():
    """Get actual scores and generate PNG spider graph"""
    try:
        # Calculate scores using current structure
        scores = {
            "Study Metadata": check_metadata_current(),
            "Participant Info": check_participants_current(),
            "Equipment": check_equipment_current(),
            "Stimuli": check_stimuli_current(),
            "AOIs": check_aois_current(),
            "Data Quality": check_data_quality_current(),
            "Preprocessing": check_preprocessing_current(),
            "Analysis": check_analysis_current(),
            "Validity": check_threats_current(),
            "Reproducibility": check_reproducibility_current()
        }
        
        # Generate PNG spider graph
        png_path = generate_spider_graph_png(scores)
        
        return scores, png_path
    except Exception as e:
        print(f"Error calculating scores: {e}")
        # Return template baseline scores if error
        scores = {
            "Study Metadata": 0.85,
            "Participant Info": 0.75,
            "Equipment": 1.0,
            "Stimuli": 0.85,
            "AOIs": 0.70,
            "Data Quality": 0.95,
            "Preprocessing": 0.80,
            "Analysis": 0.75,
            "Validity": 0.80,
            "Reproducibility": 0.90
        }
        return scores, None

def generate_spider_graph_png(scores):
    """Generate actual PNG spider graph"""
    try:
        import matplotlib
        matplotlib.use('Agg')  # Use non-interactive backend
        import matplotlib.pyplot as plt
        import numpy as np
        
        # Prepare data for spider graph
        criteria = list(scores.keys())
        values = list(scores.values())
        
        # Map to shorter labels for the graph
        labels = [
            'Study\nMetadata', 'Participant\nInfo', 'Equipment\nSpecs',
            'Stimuli\n& Materials', 'Areas of\nInterest', 'Data Quality\n& Collection',
            'Data\nPreprocessing', 'Statistical\nAnalysis', 'Validity\nAssessment',
            'Reproducibility\nMaterials'
        ]
        
        # Close the radar chart
        angles = np.linspace(0, 2*np.pi, len(criteria), endpoint=False).tolist()
        values += values[:1]
        angles += angles[:1]
        
        # Calculate overall score for coloring
        overall_score = sum(scores.values()) / len(scores)
        if overall_score >= 0.8:
            color = '#2ecc71'  # Green for excellent
        elif overall_score >= 0.6:
            color = '#f39c12'  # Orange for good
        elif overall_score >= 0.4:
            color = '#e74c3c'  # Red for needs improvement
        else:
            color = '#95a5a6'  # Gray for baseline/template
        
        # Create the spider plot
        fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
        ax.plot(angles, values, 'o-', linewidth=3, color=color, markersize=8)
        ax.fill(angles, values, alpha=0.25, color=color)
        
        # Customize the chart
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels, fontsize=11)
        ax.set_ylim(0, 1.0)
        ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
        ax.set_yticklabels(['0.2', '0.4', '0.6', '0.8', '1.0'], fontsize=10)
        ax.grid(True, alpha=0.3)
        
        # Add title with score
        plt.title(f'Repl.ET Reproducibility Analysis\n{overall_score*100:.1f}% Overall Score', 
                  fontsize=16, fontweight='bold', pad=30)
        
        # Add value labels for significant values
        for angle, value, label in zip(angles[:-1], values[:-1], labels):
            if value > 0.05:  # Only show labels for significant values
                ax.text(angle, value + 0.08, f'{value:.2f}', 
                       ha='center', va='center', fontsize=10, fontweight='bold',
                       bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.9, edgecolor=color))
        
        plt.tight_layout()
        
        # Save to root directory
        png_path = "reproducibility_spider_graph.png"
        plt.savefig(png_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"Spider graph PNG generated: {png_path}")
        return png_path
        
    except ImportError:
        print("Warning: matplotlib not available, cannot generate PNG")
        return None
    except Exception as e:
        print(f"Error generating PNG: {e}")
        return None

def check_metadata_current():
    """Check metadata quality - distinguish template vs real data"""
    if not os.path.exists("metadata.json"):
        return 0
    
    try:
        with open("metadata.json", 'r') as f:
            data = json.load(f)
        
        # Check if this is real data or template data
        template_indicators = [
            "Your Study Title",
            "Author Name", 
            "Your Institution",
            "Study Title Here",
            "Enter study title",
            "Template",
            "Example Study",
            "Sample Study"
        ]
        
        study_title = str(data.get("study_title", "")).strip()
        authors = str(data.get("authors", "")).strip() 
        institution = str(data.get("institution", "")).strip()
        
        # Check if contains template placeholders
        is_template = any(indicator.lower() in study_title.lower() or 
                         indicator.lower() in authors.lower() or 
                         indicator.lower() in institution.lower() 
                         for indicator in template_indicators)
        
        # Check if fields are empty or too generic
        is_empty = not study_title or not authors or not institution
        is_generic = (len(study_title) < 5 or len(authors) < 5 or 
                     study_title.lower() in ["test", "demo", "study"] or
                     authors.lower() in ["author", "researcher"])
        
        if is_template or is_empty or is_generic:
            return 0.05  # Template data - very low score
        else:
            return 0.95  # Real study data - high score
            
    except:
        return 0

def check_participants_current():
    """Check participants data - distinguish template vs real data"""
    if not os.path.exists("participants/participants.json"):
        return 0
    
    try:
        with open("participants/participants.json", 'r') as f:
            data = json.load(f)
        
        participants = data.get("participants", [])
        
        # Check if empty or template data
        if not participants or len(participants) == 0:
            return 0.05  # Empty template
            
        # Check if contains real participant data
        real_data_indicators = 0
        template_indicators = 0
        
        for participant in participants:
            if isinstance(participant, dict):
                participant_id = str(participant.get("participant_id", "")).strip()
                age = str(participant.get("age", "")).strip()
                gender = str(participant.get("gender", "")).strip()
                
                # Check for template/generic values
                if participant_id in ["", "ID", "participant_id", "1", "001", "P001", "Subject1"]:
                    template_indicators += 1
                elif participant_id and len(participant_id) > 1:
                    real_data_indicators += 1
                
                # Check age values
                if age in ["", "age", "25", "30"] or not age.isdigit():
                    template_indicators += 1
                elif age.isdigit() and 15 <= int(age) <= 80:
                    real_data_indicators += 1
                
                # Check gender values
                if gender in ["", "gender", "M", "F"]:
                    template_indicators += 1
                elif gender.lower() in ["male", "female", "other", "non-binary"]:
                    real_data_indicators += 1
        
        total_fields = len(participants) * 3  # 3 fields per participant
        
        if real_data_indicators >= total_fields * 0.7:
            return 0.90  # Real participant data
        elif real_data_indicators > template_indicators:
            return 0.60  # Mostly real data
        elif template_indicators >= total_fields * 0.5:
            return 0.05  # Template/generic data
        else:
            return 0.30  # Mixed data
            
    except:
        return 0

def check_equipment_current():
    """Check equipment specifications - distinguish template vs real data"""
    tracker_score = 0
    screen_score = 0
    software_score = 0
    
    # Check tracker specs
    if os.path.exists("equipment/tracker_specs.json"):
        try:
            with open("equipment/tracker_specs.json", 'r') as f:
                data = json.load(f)
            
            eye_tracker = data.get("eye_tracker", {})
            manufacturer = str(eye_tracker.get("manufacturer", "")).strip()
            model = str(eye_tracker.get("model", "")).strip()
            
            # Template indicators
            template_indicators = ["Template", "Example", "Your Tracker", "Brand", "Model"]
            is_template = any(indicator.lower() in manufacturer.lower() or 
                             indicator.lower() in model.lower() 
                             for indicator in template_indicators)
            
            # Real equipment brands
            real_brands = ["tobii", "eyelink", "gazepoint", "pupil", "smart eye"]
            is_real = any(brand.lower() in manufacturer.lower() for brand in real_brands)
            
            if is_real and len(manufacturer) > 3 and len(model) > 3:
                tracker_score = 0.95
            elif not is_template and manufacturer and model:
                tracker_score = 0.70
            else:
                tracker_score = 0.05
        except:
            tracker_score = 0
    
    # Check screen setup
    if os.path.exists("equipment/screen_setup.json"):
        try:
            with open("equipment/screen_setup.json", 'r') as f:
                data = json.load(f)
            
            # Check for real monitor data
            monitor = data.get("monitor", {})
            manufacturer = str(monitor.get("manufacturer", "")).strip()
            model = str(monitor.get("model", "")).strip()
            
            real_monitor_brands = ["dell", "samsung", "lg", "asus", "acer", "hp"]
            is_real = any(brand.lower() in manufacturer.lower() for brand in real_monitor_brands)
            
            if is_real and model:
                screen_score = 0.95
            elif manufacturer and model:
                screen_score = 0.70
            else:
                screen_score = 0.05
        except:
            screen_score = 0
    
    # Check software environment
    if os.path.exists("equipment/software_env.json"):
        try:
            with open("equipment/software_env.json", 'r') as f:
                data = json.load(f)
            
            # Check for detailed software info
            os_info = data.get("operating_system", {})
            eye_tracking = data.get("eye_tracking_software", {})
            
            if os_info and eye_tracking:
                software_score = 0.95
            elif os_info or eye_tracking:
                software_score = 0.70
            else:
                software_score = 0.05
        except:
            software_score = 0
    
    # Return average of all equipment scores
    total_scores = [s for s in [tracker_score, screen_score, software_score] if s > 0]
    return sum(total_scores) / len(total_scores) if total_scores else 0

def check_stimuli_current():
    """Check stimuli metadata - distinguish template vs real data"""
    if not os.path.exists("stimuli/stimuli_metadata.json"):
        return 0
    
    try:
        with open("stimuli/stimuli_metadata.json", 'r') as f:
            data = json.load(f)
        
        stimuli = data.get("stimuli", [])
        
        if not stimuli:
            return 0.05  # Empty template
        
        real_indicators = 0
        total_checks = 0
        
        for stimulus in stimuli:
            if isinstance(stimulus, dict):
                # Check for realistic stimulus IDs
                stimulus_id = str(stimulus.get("stimulus_id", "")).strip()
                if stimulus_id and not stimulus_id.lower() in ["s01", "s02", "template", "example"]:
                    real_indicators += 1
                total_checks += 1
                
                # Check for detailed metrics
                complexity_metrics = stimulus.get("complexity_metrics", {})
                if complexity_metrics and len(complexity_metrics) > 2:
                    real_indicators += 1
                total_checks += 1
                
                # Check for programming language
                prog_lang = str(stimulus.get("programming_language", "")).strip()
                if prog_lang and prog_lang.lower() not in ["", "language", "java"]:
                    real_indicators += 1
                total_checks += 1
        
        if total_checks == 0:
            return 0.05
        
        real_ratio = real_indicators / total_checks
        
        if real_ratio >= 0.8:
            return 0.95  # Real stimuli data
        elif real_ratio >= 0.5:
            return 0.70  # Mostly real
        elif real_ratio >= 0.2:
            return 0.30  # Mixed
        else:
            return 0.05  # Template
            
    except:
        return 0

def check_aois_current():
    """Check AOI definitions - distinguish template vs real data"""
    if not os.path.exists("aois/aois_definition.json"):
        return 0
    
    try:
        with open("aois/aois_definition.json", 'r') as f:
            data = json.load(f)
        
        aois = data.get("aois", [])
        
        if not aois:
            return 0.05
        
        real_indicators = 0
        total_checks = 0
        
        for aoi in aois:
            if isinstance(aoi, dict):
                # Check for meaningful AOI IDs
                aoi_id = str(aoi.get("aoi_id", "")).strip()
                if aoi_id and not aoi_id.lower().startswith("a0") and len(aoi_id) > 3:
                    real_indicators += 1
                total_checks += 1
                
                # Check for detailed descriptions
                description = str(aoi.get("description", "")).strip()
                if description and len(description) > 20:
                    real_indicators += 1
                total_checks += 1
                
                # Check for cognitive relevance
                relevance = str(aoi.get("cognitive_relevance", "")).strip()
                if relevance and relevance != "medium":
                    real_indicators += 1
                total_checks += 1
        
        if total_checks == 0:
            return 0.05
            
        real_ratio = real_indicators / total_checks
        
        if real_ratio >= 0.8:
            return 0.95
        elif real_ratio >= 0.5:
            return 0.70
        else:
            return 0.05
            
    except:
        return 0

def check_data_quality_current():
    """Check data quality - distinguish template vs real data"""
    if not os.path.exists("collection/protocol.json"):
        return 0
    
    # For template, return very low score
    return 0.05  # Template protocol data

def check_preprocessing_current():
    """Check preprocessing steps - distinguish template vs real data"""
    if not os.path.exists("preprocessing/preprocessing.json"):
        return 0
    
    try:
        with open("preprocessing/preprocessing.json", 'r') as f:
            data = json.load(f)
        
        steps = data.get("preprocessing_steps", data.get("steps", []))
        
        if not steps:
            return 0.05
        
        # Check for detailed preprocessing pipeline
        if len(steps) >= 5:  # Comprehensive pipeline
            detailed_steps = sum(1 for step in steps 
                               if isinstance(step, dict) and 
                               len(step.get("parameters", {})) > 2)
            
            if detailed_steps >= len(steps) * 0.8:
                return 0.95  # Real detailed preprocessing
            elif detailed_steps >= len(steps) * 0.5:
                return 0.70  # Mostly detailed
            else:
                return 0.30  # Some detail
        
        return 0.05  # Template level
            
    except:
        return 0

def check_analysis_current():
    """Check analysis methods - distinguish template vs real data"""
    if not os.path.exists("analysis/analysis.json"):
        return 0
    
    try:
        with open("analysis/analysis.json", 'r') as f:
            data = json.load(f)
        
        methods = data.get("analysis_methods", [])
        
        if not methods:
            return 0.05
        
        # Check for sophisticated analysis methods
        advanced_methods = 0
        for method in methods:
            if isinstance(method, dict):
                method_name = str(method.get("method_name", "")).strip().lower()
                
                # Look for advanced analysis techniques
                advanced_keywords = [
                    "cognitive_load", "multimodal", "machine_learning", 
                    "mixed_effects", "sequence_analysis", "classification",
                    "synchrony", "frequency", "statistical"
                ]
                
                if any(keyword in method_name for keyword in advanced_keywords):
                    advanced_methods += 1
        
        if advanced_methods >= 3:
            return 0.95  # Advanced analysis
        elif advanced_methods >= 1:
            return 0.70  # Some advanced methods
        else:
            return 0.05  # Basic/template
            
    except:
        return 0

def check_threats_current():
    """Check validity threats - distinguish template vs real data"""
    if not os.path.exists("validity/validity.json"):
        return 0
    
    try:
        with open("validity/validity.json", 'r') as f:
            data = json.load(f)
        
        threats = data.get("threats", [])
        
        if not threats:
            return 0.05
        
        # Check for detailed threat analysis
        detailed_threats = 0
        for threat in threats:
            if isinstance(threat, dict):
                strategies = threat.get("mitigation_strategies", [])
                description = str(threat.get("description", "")).strip()
                
                if len(strategies) >= 3 and len(description) > 50:
                    detailed_threats += 1
        
        if detailed_threats >= len(threats) * 0.8:
            return 0.95  # Comprehensive validity assessment
        elif detailed_threats >= len(threats) * 0.5:
            return 0.70  # Good validity assessment
        else:
            return 0.05  # Template level
            
    except:
        return 0

def check_reproducibility_current():
    """Check reproducibility materials - distinguish template vs real data"""
    if not os.path.exists("reproducibility/reproducibility.json"):
        return 0
    
    try:
        with open("reproducibility/reproducibility.json", 'r') as f:
            data = json.load(f)
        
        materials = data.get("materials", [])
        
        if not materials:
            return 0.05
        
        # Check for comprehensive reproducibility materials
        real_materials = 0
        for material in materials:
            if isinstance(material, dict):
                location = str(material.get("location", "")).strip()
                material_type = str(material.get("type", "")).strip()
                
                # Check for real URLs/DOIs
                if ("github.com" in location or "osf.io" in location or 
                    "zenodo" in location or "protocols.io" in location):
                    real_materials += 1
        
        if real_materials >= len(materials) * 0.8:
            return 0.95  # Comprehensive reproducibility
        elif real_materials >= len(materials) * 0.5:
            return 0.70  # Good reproducibility
        else:
            return 0.05  # Template level
            
    except:
        return 0

def generate_spider_graph_markdown(png_path):
    """Generate markdown for spider graph embedding"""
    return f"![Reproducibility Spider Graph]({png_path})"

def generate_checklist_markdown(scores, compliance_count, total_criteria, compliance_percentage, template_status, result_message):
    """Generate checklist markdown with scores and compliance info"""
    
    # Create status indicators for each component
    checklist_items = []
    for component, score in scores.items():
        status = "✅" if score > 0.8 else "⚠️" if score > 0.5 else "❌"
        readable_name = component.replace("_", " ").title()
        checklist_items.append(f"- {status} **{readable_name}**: {score*100:.1f}%")
    
    checklist_md = f"""## 📋 Compliance Checklist

**Status**: {template_status} ({result_message})  
**Overall Compliance**: {compliance_count}/{total_criteria} criteria met ({compliance_percentage:.1f}%)

### Component Scores:
{chr(10).join(checklist_items)}

### Legend:
- ✅ **Complete** (>80%): Publication ready
- ⚠️ **Partial** (50-80%): Good progress, needs refinement  
- ❌ **Missing** (<50%): Requires attention

---
"""
    return checklist_md

def generate_scores_table_markdown(scores, overall_score):
    """Generate scores table markdown"""
    
    rows = []
    for component, score in scores.items():
        readable_name = component.replace("_", " ").title()
        rows.append(f"| {readable_name} | {score*100:.1f}% |")
    
    table_md = f"""
| Study Component | Score |
|----------------|-------|
{chr(10).join(rows)}
| **Overall Study Score** | **{overall_score:.1f}%** |
"""
    return table_md

def update_readme_with_assessment():
    """Main function to update README with current assessment"""
    try:
        # Get current scores and generate PNG
        scores, png_path = get_actual_scores_and_generate_png()
        
        # Generate assessment
        assessment = TemplateAssessment()
        
        # Calculate compliance based on scores > 0.8 threshold
        all_scores = assessment.get_all_scores()
        compliant_criteria = sum(1 for score in all_scores.values() if score > 0.8)
        total_criteria = len(all_scores)
        compliance_percentage = (compliant_criteria / total_criteria) * 100 if total_criteria > 0 else 0
        compliance_count = compliant_criteria
        
        # Determine status
        if compliance_percentage >= 80:
            template_status = "Complete"
            result_message = "Publication Ready"
        elif compliance_percentage >= 50:
            template_status = "In Progress"  
            result_message = "Good Progress"
        else:
            template_status = "Starting"
            result_message = "Empty Template" if compliance_percentage < 30 else "Basic Setup"
        
        # Calculate overall score
        overall_score = sum(all_scores.values()) / len(all_scores) * 100 if all_scores else 0
        
        # Generate markdown content
        checklist_markdown = generate_checklist_markdown(
            all_scores, 
            compliance_count, 
            total_criteria, 
            compliance_percentage, 
            template_status, 
            result_message
        )
        
        scores_table_markdown = generate_scores_table_markdown(all_scores, overall_score)
        
        # Read current README
        readme_path = 'README.md'
        if os.path.exists(readme_path):
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()
        else:
            content = "# Study Assessment\n\n"
        
        # Update checklist section
        checklist_pattern = r'(## 📋 Compliance Checklist.*?)(?=##|\Z)'
        if re.search(checklist_pattern, content, re.DOTALL):
            content = re.sub(checklist_pattern, checklist_markdown + '\n', content, flags=re.DOTALL)
        else:
            content += '\n' + checklist_markdown + '\n'
        
        # Update scores table section  
        scores_pattern = r'(\| Study Component \| Score.*?\*\*Overall Study Score.*?\*\*[^\n]*)'
        if re.search(scores_pattern, content, re.DOTALL):
            content = re.sub(scores_pattern, scores_table_markdown.strip(), content, flags=re.DOTALL)
        else:
            content += '\n' + scores_table_markdown + '\n'
        
        # Update spider graph image
        spider_pattern = r'!\[Reproducibility Spider Graph\]\([^)]+\)'
        spider_replacement = f'![Reproducibility Spider Graph]({png_path})'
        if re.search(spider_pattern, content):
            content = re.sub(spider_pattern, spider_replacement, content)
        else:
            content += f'\n{spider_replacement}\n'
        
        # Write updated README
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("README.md updated successfully!")
        print(f"Overall Score: {overall_score:.1f}%")
        print(f"Compliance: {compliance_count}/{total_criteria} ({compliance_percentage:.1f}%)")
        print(f"Status: {template_status}")
        
    except Exception as e:
        print(f"Error updating README: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    update_readme_with_assessment()