#!/bin/bash
set -e
poetry export  --without-hashes -f requirements.txt --output requirements.txt --only main