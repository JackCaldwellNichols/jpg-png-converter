import os
import sys
from PIL import Image
import pathlib

a = input("1: ")
b = input("2: ")


#a = sys.argv[1]
#b = sys.argv[2]


def jpg_to_png(a, b):
    if os.path.exists(f'{b}/'):
        for file in os.listdir(f'{a}/'):
            filename = os.fsdecode(file)
            new_image = Image.open(f'{a}/{filename}')
            new_image.save(f'{b}/{filename.split(".")[0]}.png')
            print(f"New file {filename} created and added to the directory '{b}'")
    else:
        p = pathlib.Path(f'{b}/')
        p.mkdir(parents=True, exist_ok=True)
        for file in os.listdir(f'./{a}'):
            filename = os.fsdecode(file)
            new_image = Image.open(f'{a}/{filename}')
            new_image.save(f'{p}/{filename.split(".")[0]}.png', 'png')
            print(f"New file created and added to the directory '{b}'")


jpg_to_png(a, b)
