from pathlib import Path
import re

BASE = Path("imgs")


def get_next_id(category_path: Path):
    """
    Finds the next numeric ID inside a category folder.
    Example: 0001-peixes, 0002-aries → returns 3
    """

    max_id = 0
    pattern = re.compile(r"(\d+)-")

    if category_path.exists():
        for folder in category_path.iterdir():
            if folder.is_dir():
                match = pattern.match(folder.name)
                if match:
                    num = int(match.group(1))
                    if num > max_id:
                        max_id = num

    return max_id + 1


def create_product_folder(category: str, product_name: str):
    category_path = BASE / category

    # 1. ensure category exists
    category_path.mkdir(parents=True, exist_ok=True)

    # 2. find next ID inside category
    next_id = get_next_id(category_path)

    # 3. build folder name
    folder_name = f"{next_id:04d}-{product_name}"

    final_path = category_path / folder_name

    # safety check (rare edge case)
    if final_path.exists():
        print(f"⚠ Folder already exists: {final_path}")
        return final_path

    final_path.mkdir()
    print(f"Created: {final_path}")

    return final_path


# Example usage
create_product_folder("signos", "peixes")
