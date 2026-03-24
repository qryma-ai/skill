# Platform Deployment Guide

This guide will help you deploy the Qryma Search skill to various skill platforms.

## Prerequisites

1. **Git repository** - Create a public GitHub repository
2. **API key management** - Ensure your Qryma API key is configured correctly
3. **Dependencies installed** - Run `pip install -r requirements.txt`

## OpenClaw (Current platform)

The skill is already configured for OpenClaw. It should be in your `~/.openclaw/skills/` directory.

## Skills.sh

### 1. Create a GitHub repository
```bash
# Initialize repository
git init
git add .
git commit -m "Initial commit - Qryma Search skill"

# Create remote repository (on GitHub)
# Then:
git remote add origin https://github.com/your-username/openclaw-qryma-search.git
git push -u origin main
```

### 2. Install Skills CLI
```bash
npm install -g @skills-cli/core
```

### 3. Register and deploy
```bash
# Login to skills.sh
skills login

# Deploy your skill
skills deploy --repo https://github.com/your-username/openclaw-qryma-search.git
```

## ClawHub.ai

### Deployment steps
```bash
# Create a ClawHub account (if not done)
# https://clawhub.ai/

# Fork the repository
# Visit: https://github.com/your-username/openclaw-qryma-search
# Click "Fork"

# Create a Pull Request
# On ClawHub, create a PR to add your skill
```

### Required files
- `SKILL.md` - Detailed skill specification
- `skill.json` - OpenClaw manifest
- `manifest.json` - Generic manifest

## SkillStore.io

### 1. Prepare for submission
```bash
# Create a release package
zip -r qryma-search-v1.0.0.zip \
  main_claw.py \
  SKILL.md \
  skill.json \
  manifest.json \
  package.json \
  setup.py \
  requirements.txt \
  README.md \
  src/
```

### 2. Submit
1. Visit https://skillstore.io/submit
2. Fill out the submission form
3. Upload the zip file
4. Wait for approval

## SkillsMP.com

### Deployment
```bash
# Register an account
# https://skillsmp.com/register

# Create a new skill
# Go to Dashboard > New Skill
# Fill in:
# - Name: Qryma Search
# - Description: Web search with AI answers
# - Type: Search
# - Language: Python 3.8+

# Upload files
# Upload all files or provide GitHub URL
```

## Skill-CN.com

### China-specific platform
1. **Register an account** on https://www.skill-cn.com/
2. **Prepare documentation in Chinese** (optional but recommended)
3. **Submit for review** through their web interface

## Tencent SkillHub (skillhub.tencent.com)

### Enterprise platform
1. **Get access** - Contact Tencent's SkillHub team
2. **Prepare compliance documents**
3. **Deploy using Tencent Cloud CLI**

## Best Practices

### 1. Keep all manifest files updated
```bash
# Whenever you update the skill:
# 1. Update version in package.json, manifest.json, skill.json, and setup.py
# 2. Update description in README.md, SKILL.md
```

### 2. Test on all platforms
```bash
# Test basic functionality
python main_claw.py --query "test" --max-results 3 --format md

# Test different output formats
python main_claw.py --query "test" --format raw
python main_claw.py --query "test" --format brave
```

### 3. Monitor for changes
- Check each platform's guidelines regularly
- Update dependencies quarterly
- Test compatibility with new Python versions

## Troubleshooting

### Platform cannot detect the skill
- Check manifest.json structure
- Verify repository visibility
- Ensure all required files are present

### Skills.sh deployment fails
```bash
# Check for errors
skills deploy --repo https://github.com/your-username/openclaw-qryma-search.git --verbose

# Verify your npm package
npm list -g @skills-cli/core
```

### ClawHub integration issues
- Check PR requirements
- Verify your fork is up to date
- Check for file format issues

## Future Improvements

### Add CI/CD
```yaml
# .github/workflows/deploy.yml
name: Deploy to Platforms

on: [release]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Deploy to skills.sh
      run: npx skills deploy --repo ${{ github.repository }} --token ${{ secrets.SKILLS_TOKEN }}
```

### Add platform-specific adapters
```python
# src/adapters/skills_sh_adapter.py
class SkillsSHAdapter:
    def __init__(self, core):
        self.core = core

    def run(self, params):
        return self.core.search(**params)
```

## License

MIT
