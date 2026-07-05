from pathlib import Path

# Change these paths
SOURCE_DIR = Path("/home/dios/Resources/Website/main/imgs")
DEST_DIR = Path("/home/dios/Resources/Website/main/vds")

# Create destination if it doesn't exist
DEST_DIR.mkdir(parents=True, exist_ok=True)

for folder in SOURCE_DIR.rglob("*"):
    if folder.is_dir():
        relative = folder.relative_to(SOURCE_DIR)
        destination_folder = DEST_DIR / relative

        if not destination_folder.exists():
            destination_folder.mkdir(parents=True)
            print(f"Created: {destination_folder}")
        else:
            print(f"Already exists: {destination_folder}")

print("Done!")
