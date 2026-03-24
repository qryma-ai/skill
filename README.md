# Qryma Agent Skills

Web search with multiple output formats, AI answers, and language support — powered by the Qryma API.

## Installation

### Install Skills
For OpenClaw platform:
```bash
# The skill is automatically available if:
# 1. It's located in the ~/.openclaw/skills directory
# 2. Or the directory is added to extraDirs in openclaw.json
```

For other platforms:
```bash
cd openclaw-qryma-search
pip install -r requirements.txt
```

### Authenticate

```bash
# Environment variable
export QRYMA_API_KEY="ak-your-api-key-here"

# Or create ~/.openclaw/.env file
echo 'QRYMA_API_KEY=ak-your-api-key-here' > ~/.openclaw/.env
```

Get an API key from your Qryma service provider.

## Available Skills

### OpenClaw Qryma Search

**Skill: `openclaw-qryma-search`** - Web search with AI-optimized results

#### Command-line Usage
```bash
python main_claw.py --help
```

#### Options
| Option | Description |
|--------|-------------|
| `--query` | **Required** Search query (e.g. "machine learning") |
| `--max-results` | Maximum number of results (default: 5) |
| `--include-answer` | Include AI-generated answer (default: False) |
| `--search-depth` | Search depth: basic/advanced (default: basic) |
| `--format` | Output format: raw | brave | md (default: raw) |

## Usage Examples

### Basic Search
```bash
python main_claw.py --query "how to learn python" --format md
```

### Search with AI Answer
```bash
python main_claw.py --query "explain quantum computing" --include-answer --format md
```

### JSON Output
```bash
python main_claw.py --query "latest AI trends 2024" --format raw
```

### Advanced Search
```bash
python main_claw.py --query "artificial intelligence ethics" --max-results 10 --search-depth advanced --format brave
```

## Output Formats

### Markdown (`--format md`)
```markdown
1. Result Title
https://example.com
- Result snippet...
```

### Brave Format (`--format brave`)
```json
{
  "query": "search query",
  "results": [
    {
      "title": "Title",
      "url": "https://example.com",
      "snippet": "Result snippet..."
    }
  ]
}
```

### Raw JSON (`--format raw`)
```json
{
  "query": "search query",
  "answer": "AI-generated answer",
  "results": [
    {
      "title": "Title",
      "url": "https://example.com",
      "content": "Result snippet..."
    }
  ]
}
```

## Project Structure
```
openclaw-qryma-search/
├── main_claw.py              # Entry point
├── SKILL.md                  # Detailed skill specification
├── skill.json                # Skill manifest
├── requirements.txt          # Dependencies
├── .env.example              # Environment template
└── src/
    ├── search_core.py        # Core search logic
    ├── main.py               # Multi-platform entry point
    └── adapters/
        ├── openclaw_adapter.py   # OpenClaw platform adapter
        └── generic_adapter.py    # Generic platform adapter
```

## License

MIT
