#!/usr/bin/env bash
# run.sh

set -e

echo "iniciando gunicorn en render..."
gunicorn app:app --workers 1 --threads 5

