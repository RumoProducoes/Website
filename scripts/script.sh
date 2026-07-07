#!/usr/bin/env bash

shopt -s nullglob nocasematch

# Ask for the directory
read -rp "Enter the directory path: " TARGET_DIR

# Remove trailing slash if present
TARGET_DIR="${TARGET_DIR%/}"

# Check if it exists
if [[ ! -d "$TARGET_DIR" ]]; then
    echo "Error: '$TARGET_DIR' is not a valid directory."
    exit 1
fi

for file in "$TARGET_DIR"/*; do
    # Skip directories
    [[ -f "$file" ]] || continue

    filename="$(basename "$file")"
    extension="${filename##*.}"
    basename="${filename%.*}"

    # Skip videos
    [[ "$extension" =~ ^(mp4|webm)$ ]] && continue

    # Skip files containing left, right or front
    [[ "$basename" =~ (left|right|front) ]] && continue

    # Create directory if it doesn't exist
    mkdir -p "$TARGET_DIR/$basename"

    # Move and rename
    mv -- "$file" "$TARGET_DIR/$basename/main.$extension"
done

echo "Done!"
