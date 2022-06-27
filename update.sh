#!/usr/bin/env bash
# This script updates the production deployment of rshell.sh.

# Bash Strict Mode
set -eo pipefail

cd ~/public_html/rshell.sh

# Pull Updates
git pull

# Source Venv
source venv/bin/activate

# Update Reqs 
pip3 install -r requirements.txt

# Run Tests
python -m pytest -vv

# Restart WebApp
kill -9 `pgrep -f rshell.sh`
