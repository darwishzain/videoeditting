#!/bin/sh

# Check if project name is given
if [ -z "$1" ]; then
  echo "Usage: $0 <ProjectName>"
  exit 1
fi

PROJECT_NAME="$1"
DATE=$(date +%Y-%m-%d)
ROOT_DIR="./projects/${PROJECT_NAME}_${DATE}"

# Create base directory
mkdir -p "$ROOT_DIR"

# Create subdirectories
mkdir -p "$ROOT_DIR"/{project,footage_raw,footage_proxy,audio/music,audio/sfx,audio/voice,graphics,exports,renders_wip,reference}

echo "Project directory structure created at: $ROOT_DIR"
echo "(Note: Git is ignoring ./projects/, so your video files won't be tracked.)"
