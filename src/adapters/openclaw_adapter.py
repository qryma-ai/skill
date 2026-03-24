#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OpenClaw Platform Adapter
"""
import argparse
import json
import sys
from typing import List, Dict, Any

# Try relative import, fall back to absolute import if failed
try:
    from ..search_core import QrymaSearchCore
except (ImportError, ValueError):
    # Use absolute import when running as standalone script
    import os
    import sys
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if current_dir not in sys.path:
        sys.path.insert(0, current_dir)
    from search_core import QrymaSearchCore


def main():
    """Main entry point for the skill"""
    adapter = OpenClawAdapter()
    parser = OpenClawAdapter.create_parser()
    args = parser.parse_args()
    adapter.run(args)


def to_brave_like(obj: dict) -> dict:
    """Convert to Brave search-like format (title/url/snippet)"""
    results = []
    for r in obj.get("results", []) or []:
        results.append(
            {
                "title": r.get("title"),
                "url": r.get("url"),
                "snippet": r.get("content"),
            }
        )
    out = {"query": obj.get("query"), "results": results}
    if "answer" in obj:
        out["answer"] = obj.get("answer")
    return out


def to_markdown(obj: dict) -> str:
    """Convert to Markdown format"""
    lines = []
    if obj.get("answer"):
        lines.append(obj["answer"].strip())
        lines.append("")

    for i, r in enumerate(obj.get("results", []) or [], 1):
        title = (r.get("title") or "").strip() or r.get("url") or "(no title)"
        url = r.get("url") or ""
        snippet = (r.get("content") or "").strip()

        lines.append(f"{i}. {title}")
        if url:
            lines.append(f" {url}")
        if snippet:
            lines.append(f" - {snippet}")

    return "\n".join(lines).strip() + "\n"


class OpenClawAdapter:
    """OpenClaw adapter"""

    def __init__(self, core: QrymaSearchCore = None):
        self.core = core or QrymaSearchCore()

    def run(self, args: argparse.Namespace) -> None:
        """Execute search"""
        try:
            result = self.core.search(
                query=args.query,
                max_results=args.max_results,
                include_answer=args.include_answer,
                search_depth=args.search_depth,
            )

            if args.format == "md":
                output = to_markdown(result)
                sys.stdout.write(output)
            elif args.format == "brave":
                result = to_brave_like(result)
                json.dump(result, sys.stdout, ensure_ascii=False)
                sys.stdout.write("\n")
            else:
                json.dump(result, sys.stdout, ensure_ascii=False)
                sys.stdout.write("\n")

        except Exception as e:
            raise SystemExit(f"Error: {e}")

    @staticmethod
    def create_parser() -> argparse.ArgumentParser:
        """Create command line parser"""
        parser = argparse.ArgumentParser(
            description="Qryma search tool for OpenClaw "
        )
        parser.add_argument("--query", required=True, help="Search query")
        parser.add_argument(
            "--max-results",
            type=int,
            default=5,
            help="Maximum number of results",
        )
        parser.add_argument(
            "--include-answer",
            action="store_true",
            help="Include AI answer",
        )
        parser.add_argument(
            "--search-depth",
            default="basic",
            choices=["basic", "advanced"],
            help="Search depth",
        )
        parser.add_argument(
            "--format",
            default="raw",
            choices=["raw", "brave", "md"],
            help="Output format: raw | brave | md",
        )
        return parser


if __name__ == "__main__":
    main()
