import sys
from pathlib import Path

ALLOWED_EXT = {".jpg", ".jpeg", ".png", ".webp"}

def rename_folder(folder: Path):
    images = [
        f for f in folder.iterdir()
        if f.is_file() and f.suffix.lower() in ALLOWED_EXT
    ]

    if not images:
        return

    print(f"\nProcessing: {folder}")

    for img in images:
        name = img.stem.lower()

        # MAIN IMAGE
        if name == "main":
            img.rename(folder / "main.webp")
            print(f"{img.name} → main.webp")

        # NUMBERED IMAGES
        elif name.isdigit():
            num = int(name)
            new_name = f"mod_{num}.webp"
            img.rename(folder / new_name)
            print(f"{img.name} → {new_name}")

        else:
            print(f"Skipped: {img.name}")


def walk(base: Path):
    for folder in base.rglob("*"):
        if folder.is_dir():
            rename_folder(folder)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python rename_images.py imgs/")
        sys.exit(1)

    walk(Path(sys.argv[1]))
