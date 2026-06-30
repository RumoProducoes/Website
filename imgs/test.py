#!/usr/bin/env python3

from pathlib import Path
import shutil

BASE = Path.cwd()

# source file -> destination folder
PRODUCTS = {
    # -------------------------
    # ANIVERSÁRIOS
    # -------------------------
    "feliz_aniversario":
        "canecas/aniversarios/000001-feliz_aniversario",

    "feliz_aniversario_v2":
        "canecas/aniversarios/000002-feliz_aniversario_v2",

    # -------------------------
    # DATAS COMEMORATIVAS
    # -------------------------
    "feliz_dia_das_maes":
        "canecas/datas_comemorativas/000001-feliz_dia_das_maes",

    "feliz_dia_das_maes_v2":
        "canecas/datas_comemorativas/000002-feliz_dia_das_maes_v2",

    "feliz_dia_dos_pais":
        "canecas/datas_comemorativas/000003-feliz_dia_dos_pais",

    "feliz_pascoa":
        "canecas/datas_comemorativas/000004-feliz_pascoa",
}


def move_product(name, folder):

    folder = BASE / folder
    folder.mkdir(parents=True, exist_ok=True)

    webp = BASE / f"{name}.webp"
    jpeg = BASE / f"{name}.jpeg"

    if webp.exists():
        dst = folder / "main.webp"

        if dst.exists():
            print(f"SKIP {dst}")
        else:
            shutil.move(str(webp), str(dst))
            print(f"Moved {webp.name}")

    if jpeg.exists():
        dst = folder / "backup_main.jpeg"

        if dst.exists():
            print(f"SKIP {dst}")
        else:
            shutil.move(str(jpeg), str(dst))
            print(f"Moved {jpeg.name}")


def main():

    for product, folder in PRODUCTS.items():
        move_product(product, folder)

    print("\nFinished.")


if __name__ == "__main__":
    main()
