#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt
pip install --upgrade frozendict experta
pip freeze > requirements.txt
# Remove existing virtual environment
rm -rf .venv

# Create a new virtual environment
python -m venv .venv

# Activate the virtual environment
source .venv/bin/activate  # or .venv\Scripts\activate for Windows

# Install dependencies
pip install -r requirements.txt
