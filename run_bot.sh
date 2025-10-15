#!/bin/zsh
set -euo pipefail

# Decrypt .env.gpg to a temporary file and ensure it is removed on exit
TMP_ENV="$(mktemp)"
trap 'rm -f "$TMP_ENV"' EXIT

gpg --decrypt --quiet .env.gpg > "$TMP_ENV"

# Validate .env format: non-empty, non-comment lines must contain KEY=VALUE
INVALID_LINES=$(awk 'NF && $0 !~ /^[[:space:]]*#/ && $0 !~ /=/ {print NR":"$0}' "$TMP_ENV" || true)
if [ -n "$INVALID_LINES" ]; then
  echo "Error: .env contains lines without KEY=VALUE format. Please fix these line numbers:"
  echo "$INVALID_LINES" | sed 's/:.*$//' | tr '\n' ' '
  echo "\nExample expected lines: DISCORD_TOKEN=..., BOT_TOKEN=..., OPENROUTER_API_KEY=..."
  exit 1
fi

# Export env vars for the process
set -a
source "$TMP_ENV"
set +a

# Setup and activate virtual environment
if [ ! -d .venv ]; then
  python3 -m venv .venv
fi
source .venv/bin/activate

# Install dependencies (no-op if already satisfied)
pip install -r requirements.txt

# Run the bot
python3 fast_summarizer.py
