#!/bin/sh

# Check if project name is given
if [ -z "$1" ]; then
  echo "Usage: $0 <ProjectName>"
  exit 1
fi

PROJECT_NAME="$1"
DATE=$(date +%Y-%m-%d)
BASE_DIR="./projects"
ROOT_DIR="${BASE_DIR}/${PROJECT_NAME}_${DATE}"

# Ensure ./projects exists
if [ ! -d "$BASE_DIR" ]; then
  echo "Creating base directory: $BASE_DIR"
  mkdir -p "$BASE_DIR"
fi

# Create project directory
if [ -d "$ROOT_DIR" ]; then
  echo "Error: Project directory already exists: $ROOT_DIR"
  exit 1
fi

mkdir -p "$ROOT_DIR"

# Create subdirectories
mkdir -p "$ROOT_DIR/project"
mkdir -p "$ROOT_DIR/footage_raw"
mkdir -p "$ROOT_DIR/footage_proxy"
mkdir -p "$ROOT_DIR/audio/music"
mkdir -p "$ROOT_DIR/audio/sfx"
mkdir -p "$ROOT_DIR/audio/voice"
mkdir -p "$ROOT_DIR/graphics"
mkdir -p "$ROOT_DIR/exports"
mkdir -p "$ROOT_DIR/renders_wip"
mkdir -p "$ROOT_DIR/reference"

echo "✅ Project directory structure created at: $ROOT_DIR"
echo "(Note: Git is ignoring ./projects/, so your video files won't be tracked.)"
