#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generic Skill Platform Adapter (Reserved Template)
For Skills.ai / SkillStore and other platforms
"""
import argparse
import json
import sys
from typing import List, Dict, Any

from ..search_core import QrymaSearchCore


class GenericSkillAdapter:
    """Generic skill platform adapter"""

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

            # Generic skill platform output format
            output = {
                "success": True,
                "data": result,
            }

            json.dump(output, sys.stdout, ensure_ascii=False)
            sys.stdout.write("\n")

        except Exception as e:
            error_output = {
                "success": False,
                "error": str(e),
            }
            json.dump(error_output, sys.stdout, ensure_ascii=False)
            sys.stdout.write("\n")

    @staticmethod
    def create_parser() -> argparse.ArgumentParser:
        """Create command line parser"""
        parser = argparse.ArgumentParser(
            description="Qryma search tool for generic skill platforms "
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
            "--platform",
            default="generic",
            help="Target skill platform",
        )
        return parser
