# 🔗 Link Checking System

This repository has automated link checking to prevent broken links in documentation.

## 🚀 Quick Start

### Check Links Before Committing
```bash
# Run local link checker
./scripts/check-links.sh

# Install pre-commit hook (optional)
git config core.hooksPath .githooks
```

## 🔧 System Components

### 1. **GitHub Actions** (`.github/workflows/link-check.yml`)
- Runs on every push and PR
- Weekly scheduled checks
- Blocks merging if links are broken

### 2. **Local Script** (`scripts/check-links.sh`)
- Run before committing
- Checks internal file references
- Detects problematic patterns

### 3. **Pre-commit Hook** (`.githooks/pre-commit`)
- Automatically runs on `git commit`
- Install with: `git config core.hooksPath .githooks`

### 4. **Configuration** (`.github/link-check-config.json`)
- Customizes link checker behavior
- Excludes problematic patterns

## 🚫 Common Issues & Solutions

### Missing Files
- **Problem**: References to non-existent files
- **Solution**: Ensure referenced files exist or update paths

### GitHub Features Not Enabled
- **Problem**: Links to GitHub Discussions when not enabled
- **Solution**: Enable feature or use Issues instead

### Placeholder DOIs
- **Problem**: `10.5281/zenodo.placeholder` links
- **Solution**: Remove or replace with real DOI

### Generated Files Missing
- **Problem**: `outputs/reproducibility_spider_analysis.png` missing
- **Solution**: Run `python3 tools/generate_enhanced_spider_report.py`

## 📋 Best Practices

### 1. **Before Committing**
```bash
# Always check links first
./scripts/check-links.sh

# If spider analysis is missing:
python3 tools/generate_enhanced_spider_report.py
```

### 2. **File Organization**
- Keep referenced files in their expected locations
- Update all references when moving files
- Use relative paths for internal links

### 3. **External Links**
- Verify external URLs exist before adding
- Avoid linking to temporary/development URLs
- Use stable, permanent links when possible

### 4. **Documentation Updates**
- Test all new links before committing
- Update this guide when adding new link patterns
- Keep the link checker configuration updated

## 🔧 Troubleshooting

### Link Checker Fails Locally
```bash
# Check what's failing
./scripts/check-links.sh

# Common fixes:
python3 tools/generate_enhanced_spider_report.py  # Generate missing PNG
git add outputs/reproducibility_spider_analysis.png
```

### GitHub Actions Failing
1. Check the Actions tab for detailed error messages
2. Run local script to reproduce the issue
3. Fix the broken links and push again

### Adding New Link Patterns
1. Update `scripts/check-links.sh` with new checks
2. Update `.github/link-check-config.json` if needed
3. Test locally before committing

## 📞 Support

If you encounter link checking issues:
- 🐛 [Report a bug](https://github.com/fratelus/Repl.ET/issues) with the "bug" label
- 💡 [Suggest improvements](https://github.com/fratelus/Repl.ET/issues) with the "enhancement" label 