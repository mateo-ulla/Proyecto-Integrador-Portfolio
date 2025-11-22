#!/usr/bin/env bash
# run.sh

set -e

echo "iniciando gunicorn en render..."
gunicorn app:app --workers 3 --bind 0.0.0.0:$PORT
