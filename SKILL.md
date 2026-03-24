---
name: openclaw-qryma-search
description: Search the web with multiple output formats, AI answers, and language support using the Qryma API. Use this skill when the user wants to search the web, find information on a specific topic, says "search", "look up", "find information", "web search", or needs quick answers from the internet. Supports Markdown format for readability, JSON for structured data, and Brave search-like format.
---

# openclaw-qryma search

Search the web with Qryma search engine. Supports multiple output formats including Markdown, JSON, and Brave search-like format.

## Before running any command

If you don't have the skill configured, check that you have:

1. Installed dependencies:
   ```bash
   cd openclaw-qryma-search && pip install -r requirements.txt
   ```

2. Configured your API key:
   ```bash
   echo 'QRYMA_API_KEY=ak-your-api-key-here' > ~/.openclaw/.env
   ```

## When to use

Use this skill for:
- Finding information on specific topics
- Getting quick answers to questions
- Researching new topics
- Looking up definitions or explanations
- Finding articles, tutorials, or documentation

## Quick start

### Basic search (Markdown format)
```bash
python main_claw.py --query "how to learn python" --max-results 3 --format md
```

### Search with AI answer
```bash
python main_claw.py --query "explain quantum computing" --include-answer --format md
```

### JSON format output
```bash
python main_claw.py --query "latest AI trends 2024" --format raw
```

### Advanced search
```bash
python main_claw.py --query "artificial intelligence ethics" --max-results 10 --search-depth advanced --format brave
```

## Options

Option | Description
--- | ---
--query | **Required** Search query (e.g. "machine learning basics")
--max-results | Maximum number of results to return (default: 5)
--include-answer | Include AI-generated answer (default: False)
--search-depth | Search depth level: basic/advanced (default: basic)
--format | Output format: raw | brave | md (default: raw)

## Output formats

### Markdown format (--format md)
Returns clean, readable Markdown:
```markdown
1. Title of Result
https://example.com
- Result snippet...
```

### Brave format (--format brave)
Structured JSON like Brave search:
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

### Raw format (--format raw)
Complete JSON with all fields:
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

## Search strategies

### For general information
```bash
python main_claw.py --query "topic" --max-results 5 --format md
```

### For detailed research
```bash
python main_claw.py --query "detailed topic" --max-results 10 --search-depth advanced --include-answer --format md
```

### For quick answers
```bash
python main_claw.py --query "specific question" --include-answer --format md
```

## Tips

1. **Be specific**: Use detailed queries for better results
2. **Use quotes for exact phrases**: `"how to install python on Windows"`
3. **Limit results**: For quick answers, use `--max-results 3`
4. **Include answer**: For direct answers, use `--include-answer`
5. **Format for readability**: Use `--format md` for easier reading

## Configuration

### Environment variable
```bash
export QRYMA_API_KEY="ak-your-api-key-here"
```

### Configuration file
Create `~/.openclaw/.env` file:
```bash
QRYMA_API_KEY=ak-your-api-key-here
```

## Files

- `main_claw.py`: Command-line entry point
- `src/search_core.py`: Core search logic
- `src/adapters/openclaw_adapter.py`: OpenClaw platform adapter
- `src/adapters/generic_adapter.py`: Generic platform adapter

## License

MIT
