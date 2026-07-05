from pathlib import Path
import shutil
import re
import unicodedata

# Root folder containing all categories
ROOT_DIR = Path("/home/dios/Resources/Website/main/vds")

VIDEO_EXTENSIONS = {
    ".mp4",
    ".webm",
    ".mov",
    ".mkv",
    ".avi",
    ".m4v"
}


def normalize(name: str) -> str:
    """Normalize names for comparison."""

    # lowercase
    name = name.lower()

    # remove accents
    name = unicodedata.normalize("NFKD", name)
    name = "".join(c for c in name if not unicodedata.combining(c))

    # replace separators with spaces
    name = name.replace("_", " ")
    name = name.replace("-", " ")

    # remove everything except letters, numbers and spaces
    name = re.sub(r"[^a-z0-9 ]", "", name)

    # collapse multiple spaces
    name = " ".join(name.split())

    return name


for category in ROOT_DIR.iterdir():

    if not category.is_dir():
        continue

    print(f"\n========== {category.name} ==========")

    folder_lookup = {}

    # Build lookup table from folders
    for folder in category.iterdir():

        if not folder.is_dir():
            continue

        # remove numeric prefix
        parts = folder.name.split("-", 1)

        if len(parts) != 2:
            continue

        normalized = normalize(parts[1])

        folder_lookup[normalized] = folder

    # Find videos
    for file in category.iterdir():

        if not file.is_file():
            continue

        if file.suffix.lower() not in VIDEO_EXTENSIONS:
            continue

        video_name = normalize(file.stem)

        if video_name in folder_lookup:

            destination = folder_lookup[video_name] / file.name

            if destination.exists():
                print(f"Skipping (already exists): {destination.name}")
                continue

            print(f"Moving:")
            print(f"  {file.name}")
            print(f"    -> {folder_lookup[video_name].name}/")

            shutil.move(file, destination)

        else:
            print(f"No folder found for: {file.name}")

print("\nFinished!")
