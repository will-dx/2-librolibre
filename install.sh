#!/usr/bin/env bash
set -e
# Install OS dependencies required for psycopg (if binary wheels fail)
apt-get update -y && apt-get install -y libpq-dev gcc python3-dev
