#!/bin/bash
# Run SafeGuard AI development server
# Uses port 8001 if 8000 is already in use
cd "$(dirname "$0")"
if lsof -i :8000 -sTCP:LISTEN -t >/dev/null 2>&1; then
  echo "Port 8000 in use. Starting on http://127.0.0.1:8001/"
  python manage.py runserver 8001
else
  echo "Starting on http://127.0.0.1:8000/"
  python manage.py runserver
fi
