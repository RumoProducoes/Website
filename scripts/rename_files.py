import sys
from pathlib import Path

IMAGE_EXT = {".jpg", ".jpeg", ".png", ".webp"}
VIDEO_EXT = {".mp4", ".mov", ".avi", ".mkv", ".webm", ".m4v"}

def rename_folder(folder: Path):
    files = [f for f in folder.iterdir() if f.is_file()]

    images = [f for f in files if f.suffix.lower() in IMAGE_EXT]
    videos = [f for f in files if f.suffix.lower() in VIDEO_EXT]

    if not images and not videos:
        return

    print(f"\nProcessing: {folder}")

    # ==========================
    # Rename Images
    # ==========================
    for img in images:
        name = img.stem.lower()

        # MAIN IMAGE
        if name != "main" and name != "left" and name != "front" and name != "right":
            new_name = "main.webp"
            img.rename(folder / new_name)
            print(f"{img.name} → {new_name}")

        # NUMBERED IMAGES
        elif name.isdigit():
            num = int(name)
            new_name = f"mod_{num}.webp"
            img.rename(folder / new_name)
            print(f"{img.name} → {new_name}")

        else:
            print(f"Skipped: {img.name}")

    # ==========================
    # Rename Video
    # ==========================
    if videos:
        if len(videos) > 1:
            print("Warning: Multiple videos found. Only the first one will be renamed.")

        video = videos[0]
        new_name = f"360{video.suffix.lower()}"

        video.rename(folder / new_name)
        print(f"{video.name} → {new_name}")


def walk(base: Path):
    for folder in base.rglob("*"):
        if folder.is_dir():
            rename_folder(folder)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python rename_images.py imgs/")
        sys.exit(1)

    walk(Path(sys.argv[1]))
