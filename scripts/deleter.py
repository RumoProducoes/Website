from pathlib import Path

ROOT = Path.home() / "Resources/Website"

deleted = 0

for path in ROOT.rglob("*:Zone.Identifier"):
    if path.is_file():
        print(f"Deleting: {path}")
        path.unlink()
        deleted += 1

print(f"\nDone! Deleted {deleted} file(s).")
