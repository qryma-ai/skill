# OpenClaw Skill Integration Guide

This guide will help you integrate the Qryma Search tool into the OpenClaw platform.

## Table of Contents

- [Quick Start](#quick-start)
- [Skill Configuration](#skill-configuration)
- [Installation Methods](#installation-methods)
- [API Key Configuration](#api-key-configuration)
- [Usage Examples](#usage-examples)

## Quick Start

### 1. Verify Project Structure

Ensure your project structure is as follows:

```
openclaw-qryma-search/
├── skill.json              # Skill configuration manifest (new)
├── setup.py                # Python package configuration (new)
├── main_claw.py            # OpenClaw direct entry point
├── requirements.txt        # Dependencies list
├── src/
│   ├── search_core.py      # Core search logic
│   ├── main.py             # Multi-platform entry point
│   └── adapters/
│       ├── openclaw_adapter.py   # OpenClaw adapter
│       └── generic_adapter.py    # Generic adapter
└── SKILL_INTEGRATION.md    # This document
```

### 2. Install for Local Testing

```bash
cd openclaw-qryma-search

# Method 1: Development mode installation (recommended for testing)
pip install -e .

# Method 2: Regular installation
pip install .
```

After installation, you can test:

```bash
qryma-search --help
qryma-search --query "test query" --max-results 3 --format md
```

## Skill Configuration

### skill.json Description

`skill.json` is the core configuration file for OpenClaw to recognize and load the skill:

```json
{
  "name": "qryma-search",              # Skill unique identifier
  "version": "1.0.0",                   # Version number
  "title": "Qryma Search",              # Display name
  "description": "...",                  # Description
  "requires_api_key": true,              # Whether API Key is required
  "api_key_env": "QRYMA_API_KEY",       # API Key environment variable name
  "endpoint_env": "QRYMA_ENDPOINT",     # Endpoint environment variable name
  "entry_point": "main_claw.py",         # Entry file
  "language": "python",                   # Programming language
  "arguments": { ... }                    # Command-line argument definitions
}
```

### Updating skill.json

Update the following fields according to your actual needs:

1. **author**: Your team or personal name
2. **repository**: Your repository address
3. **description**: More detailed description
4. **keywords**: Related keywords

## Installation Methods

### Method 1: Direct Copy to OpenClaw Tools Directory

```bash
# 1. Find OpenClaw tools directory (usually)
# Windows: %APPDATA%\.openclaw\tools\
# macOS/Linux: ~/.openclaw/tools/

# 2. Copy project
cp -r openclaw-qryma-search ~/.openclaw/tools/qryma-search

# 3. Install dependencies
cd ~/.openclaw/tools/qryma-search
pip install -r requirements.txt
```

### Method 2: Install as Python Package

```bash
# 1. Build package
cd openclaw-qryma-search
python -m build

# 2. Install
pip install dist/qryma_search-1.0.0-py3-none-any.whl

# 3. Configure OpenClaw reference
# Add skill path in OpenClaw settings
```

### Method 3: Install via OpenClaw UI

1. Open OpenClaw
2. Go to Skills/Extensions management page
3. Click "Add Skill" or "Import Skill"
4. Select project directory or upload skill.json
5. Follow the prompts to complete installation

## API Key Configuration

### Method 1: Configure via OpenClaw UI (Recommended)

1. Find Qryma Search skill in OpenClaw
2. Click "Configure" or "Settings"
3. Enter your QRYMA_API_KEY
4. (Optional) Set QRYMA_ENDPOINT to your local backend address

### Method 2: Environment Variables

```bash
# Temporary setting (current terminal)
export QRYMA_API_KEY="ak-your-api-key-here"
export QRYMA_ENDPOINT="http://localhost:8080/api/web"  # Optional

# Permanent setting (add to ~/.bashrc, ~/.zshrc, etc.)
echo 'export QRYMA_API_KEY="ak-your-api-key-here"' >> ~/.bashrc
echo 'export QRYMA_ENDPOINT="http://localhost:8080/api/web"' >> ~/.bashrc
source ~/.bashrc
```

### Method 3: Configuration File

Create `~/.openclaw/.env` file:

```env
# Qryma Search Configuration
QRYMA_API_KEY=ak-your-api-key-here
QRYMA_ENDPOINT=http://localhost:8080/api/web
```

## Usage Examples

### Using in OpenClaw

#### Basic Search
```
# In OpenClaw command line or chat
/qryma-search query="2024 AI development trends" max-results=5
```

#### Search with AI Answer
```
/qryma-search query="explain quantum computing" include-answer=true format=md
```

#### Advanced Search
```
/qryma-search query="latest research" search-depth=advanced max-results=10
```

### Using Directly from Command Line

```bash
# Using main_claw.py
python main_claw.py --query "Python best practices" --format md

# Using installed command-line tool
qryma-search --query "machine learning" --max-results 10

# Using multi-platform entry point
python -m src.main openclaw --query "test" --format brave
```

### Using as a Python Library

```python
from src.search_core import QrymaSearchCore

# Initialize
core = QrymaSearchCore(
    api_key="ak-your-key",
    endpoint="http://localhost:8080/api/web"
)

# Execute search
result = core.search(
    query="your query",
    max_results=5,
    include_answer=True,
    search_depth="basic"
)

print(result)
```

## Output Formats

### Raw JSON (Default)
```json
{
  "query": "search query",
  "results": [
    {
      "title": "Result title",
      "url": "https://example.com",
      "content": "Result description..."
    }
  ]
}
```

### Brave Format
```json
{
  "query": "search query",
  "results": [
    {
      "title": "Result title",
      "url": "https://example.com",
      "snippet": "Result description..."
    }
  ]
}
```

### Markdown Format
```markdown
1. Result title
https://example.com
- Result description...
```

## Troubleshooting

### Problem: Skill Not Showing in OpenClaw

**Solution:**
1. Confirm skill.json is in the project root directory
2. Check if skill.json has valid JSON format
3. Restart OpenClaw
4. Check OpenClaw log files

### Problem: API Key Validation Failed (401 Unauthorized)

**Solution:**
1. Confirm API Key is correctly configured
2. Check if API Key exists and is active in the database
3. Confirm endpoint URL is correct
4. Check backend logs

### Problem: Command-line Tool Not Found

**Solution:**
1. Confirm you have run `pip install .`
2. Check if Python Scripts/bin directory is in PATH
3. Run using full path: `python -m adapters.openclaw_adapter`

## Development and Debugging

### Local Testing Mode

```bash
# Set local backend
export QRYMA_ENDPOINT="http://localhost:8080/api/web"

# Use test API Key
export QRYMA_API_KEY="ak-test-key"

# Run tests
python tests/test_local.py
```

### View Detailed Logs

Add debug output in `search_core.py`, or use:
```bash
python -u main_claw.py --query "test" 2>&1 | tee debug.log
```

## Next Steps

1. [ ] Test basic functionality in OpenClaw
2. [ ] Configure API Key and Endpoint
3. [ ] Run complete test suite
4. [ ] Prepare user documentation
5. [ ] Publish to OpenClaw Skill Store

## Technical Support

If you encounter any issues, please:
1. Check the troubleshooting section of this document
2. Check OpenClaw and backend logs
3. Submit an issue to the project repository

---

**Note**: Never commit or hardcode real API keys to the version control system!
