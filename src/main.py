#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Qryma Search Tool Main Entry - Multi-platform support
"""
import sys
import argparse


def main():
    # Parse top-level arguments
    parser = argparse.ArgumentParser(
        description="Qryma Search Tool - Multi-platform adapter support"
    )

    subparsers = parser.add_subparsers(title="Platform", dest="platform")

    # OpenClaw platform
    from adapters.openclaw_adapter import OpenClawAdapter

    openclaw_parser = subparsers.add_parser(
        "openclaw", help="OpenClaw platform interface"
    )
    OpenClawAdapter.create_parser().parse_args(namespace=openclaw_parser)

    # Add other platform adapters (example)
    # from adapters.skills_ai_adapter import SkillsAIAdapter
    # skills_ai_parser = subparsers.add_parser(
    #     "skillsai", help="Skills.ai platform interface"
    # )
    # SkillsAIAdapter.create_parser().parse_args(namespace=skills_ai_parser)

    args, unknown = parser.parse_known_args()

    if args.platform == "openclaw":
        adapter = OpenClawAdapter()
        adapter_parser = OpenClawAdapter.create_parser()
        adapter_args = adapter_parser.parse_args(unknown)
        adapter.run(adapter_args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
