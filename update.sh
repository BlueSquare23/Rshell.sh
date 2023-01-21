#!/usr/bin/env bash
# This script updates the production deployment of rshell.sh.

# Bash Strict Mode.
set -eo pipefail

cd ~/public_html/rshell.sh

# Pull Updates.
git pull

# Wipe out old virtual env and start anew.
rm -rf venv
python3 -m virtualenv venv
source venv/bin/activate

# Install Requirements.
pip3 install -r requirements.txt

# Run Tests.
python -m pytest -vv

# Restart WebApp.
kill -9 `pgrep -f rshell.sh`
