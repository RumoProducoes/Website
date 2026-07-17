from pathlib import Path
import re

# Ask the user for the directory
root = Path(input("Enter the folder path: ").strip())

if not root.exists() or not root.is_dir():
    print("Invalid directory.")
    exit(1)

pattern = re.compile(r"^(\d{6})(.*)$")

step = 4
starting_num = 34

# Sort in descending order to avoid name collisions
folders = sorted(
    [p for p in root.iterdir() if p.is_dir()],
    key=lambda p: p.name,
    reverse=True
)

for folder in folders:
    m = pattern.match(folder.name)
    if not m:
        continue

    number = int(m.group(1))
    suffix = m.group(2)

    if number >= starting_num:
        new_name = f"{number + step:06d}{suffix}"
        new_path = folder.with_name(new_name)

        print(f"{folder.name} -> {new_name}")
        folder.rename(new_path)

print("Done!")
