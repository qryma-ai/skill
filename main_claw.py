#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OpenClaw Direct Run Version
Simplified version that directly accepts command line arguments and outputs results
"""
import argparse
import sys
import os

# Add src directory to Python path to ensure modules can be imported correctly
script_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(script_dir, 'src')
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

try:
    from adapters.openclaw_adapter import OpenClawAdapter
except ImportError:
    # Fallback import method
    print("Warning: Using fallback import method", file=sys.stderr)
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "openclaw_adapter",
        os.path.join(src_dir, 'adapters', 'openclaw_adapter.py')
    )
    openclaw_adapter = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(openclaw_adapter)
    OpenClawAdapter = openclaw_adapter.OpenClawAdapter


def main():
    adapter = OpenClawAdapter()
    parser = OpenClawAdapter.create_parser()
    args = parser.parse_args()
    adapter.run(args)


def handler(event, context=None):
    """Handler function for platform integration"""
    adapter = OpenClawAdapter()
    return adapter.run(event)


if __name__ == "__main__":
    main()
