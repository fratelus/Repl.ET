# Changelog

All notable changes to this project will be documented in this file.

## [1.1.0] - 2024-12-15

### Added
- 🕷️ **Beautiful Spider Graphs**: Individual reproducibility analysis for each study
- 🤖 **Auto-updating README**: GitHub Actions automatically updates spider graph
- 📖 **Comprehensive User Guide**: Step-by-step instructions and troubleshooting
- 📚 **Organized Documentation**: Structured docs/ directory with guides
- 🎨 **Enhanced Visualization**: Color-coded scoring with value annotations
- 🔧 **Headless Support**: Matplotlib backend for CI/CD environments

### Improved
- README simplified with quick start and user guide reference
- Repository structure organized and cleaned up
- Spider graphs now show all 10 reproducibility criteria
- GitHub Actions enhanced with spider graph generation
- Documentation restructured for better navigation

### Technical
- Added `matplotlib.use('Agg')` for headless environments
- Enhanced .gitignore for better file management
- Cleaned up temporary files and cache directories
- Improved spider graph styling and readability

## [1.0.0] - 2024-12-15

### Added
- Initial release of Repl.ET template
- Comprehensive JSON schema validation
- Reproducibility scoring system
- Complete test suite with 35 tests
- Realistic demo implementation
- Documentation and compliance checklist

### Fixed
- Schema validation issues with external references
- Test coverage improvements
- Data integrity checks
