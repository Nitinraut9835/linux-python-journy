#!/bin/bash

# Check if directory argument is provided
if [ -z "$1" ]; then
    echo "Usage: ./backup.sh <directory>"
    exit 1
fi

SOURCE_DIR="$1"

# Check if directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Directory does not exist."
    exit 1
fi

# Create timestamp
DATE=$(date +"%Y-%m-%d_%H-%M-%S")

BACKUP_DIR="backup-$DATE"

# Create backup directory
mkdir "$BACKUP_DIR"

# Copy files
cp -r "$SOURCE_DIR" "$BACKUP_DIR"

echo "Backup completed: $BACKUP_DIR"
