import os
import sys
from PIL import Image
import pathlib

#a = input("1: ")
#b = input("2: ")


a = sys.argv[1]
b = sys.argv[2]


if not os.path.exists(b):
    os.mkdir(b)

for file in os.listdir(a):
    new_img = Image.open(f'{a}/{file}')
    new_img.save(f'{b}/{file.split(".")[0]}.png', 'png')
    print(f"New image saved")


