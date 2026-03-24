#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="openclaw-qryma-search",
    version="1.0.0",
    description="Qryma search engine tool for multiple platforms including OpenClaw, skills.sh, ClawHub, and more",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Qryma Team",
    author_email="support@qryma.com",
    url="https://github.com/qryma/openclaw-qryma-search",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "requests>=2.28.0",
        "python-dotenv>=1.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
    keywords=["qryma", "search", "openclaw", "web"],
    license="MIT",
)
