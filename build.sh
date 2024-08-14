#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt
pip install experta
pip freeze > requirements.txt
# Remove existing virtual environment
# rm -rf .venv
sed -i 's/from collections import Mapping/from collections.abc import Mapping/' $(pip show frozendict | grep Location | cut -d ' ' -f 2)/frozendict/__init__.py

# Create a new virtual environment
# python -m venv .venv

# Activate the virtual environment
# source .venv/bin/activate  # or .venv\Scripts\activate for Windows

# Install dependencies
pip install fastapi uvicorn
python -m pip install --upgrade pip