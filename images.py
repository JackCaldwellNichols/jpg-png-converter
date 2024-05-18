from PIL import Image
import os


def make_dir(name):
    return os.write(name)


def jpg_to_png(a, b):

    directory = os.fsencode(f'./{a}')
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        new_image = Image.open(f'{a}/{filename}')
        new_image.save(make_dir(b), 'png')

        #new_image.save(f'{filename}.png')
