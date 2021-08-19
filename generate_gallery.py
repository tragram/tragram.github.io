#!/usr/bin/env python

# install imagesize: pip install Pillow pyyaml

__author__ = 'Olivier Pieters'
__author_email__ = 'me@olivierpieters.be'
__license__ = 'BSD-3-Clause'

# edited: Dominik Hodan

import yaml
import sys
from os import listdir
from os.path import isfile, join
from PIL import Image
import pathlib

# configuration
try:
    path = sys.argv[1]
except:
    print("You need to provide folder as an argument!")
    quit()

# assume that folders that have "gallery" in their name are inside post img folder
if 'gallery' in pathlib.PurePath(path).name:
    folder_names=pathlib.PurePath(path).parts[-2:]
else:
    folder_names = [pathlib.PurePath(path).name]

output_file = f"./_data/galleries/{'-'.join(folder_names)}.yml"
input_file = output_file
extensions = ['jpg', 'png']

# set correct path

# extract image files
print('Collecting files...')
files = [f for f in listdir(path) if isfile(join(path, f))]
files = [f for f in files if f[f.rfind('.')+1:] in extensions]
# don't change previously generated files
files = [f for f in files if "--" not in f]

gallery = {}
thumbs = {}
originals = {}

#  resize and save image files
print('Renaming files...')
for f in files:
    image_name = f[:f.rfind('.')]
    img = Image.open("./assets/img/"+'/'.join(folder_names)+"/"+f)
    image_sizes = [
        2**i for i in range(13, 7, -1) if 2**i < img.width and 2**i < img.height]
    originals[image_name] = f
    gallery[image_name] = []
    for i, size in enumerate(image_sizes):
        img.thumbnail([size, size])
        if i+1 < len(image_sizes):
            filename = image_name + f"--{size}x{size}" + f[f.rfind('.'):]
            gallery[image_name].append(filename)
        else:
            filename = image_name + "--thumbnail" + f[f.rfind('.'):]
            thumbs[image_name] = filename
        img.save("./assets/img/"+'/'.join(folder_names)+"/"+filename)

# try to load YAML data
print('Checking existing YAML data...')
if isfile(input_file):
    input_gallery = yaml.load(open(input_file, 'r'))
else:
    # create empty dummy file
    input_gallery = {"pictures": []}

old_gallery = input_gallery['pictures']

# merge two data sets into one
print('Merging YAML data...')
for pic in gallery:
    found = False
    # try to find matching filename
    for i in old_gallery:
        if pic == i["filename"]:
            # i["sizes"] = gallery[pic]
            # # include thumbnail if present
            # if pic in thumbs:
            #     i["thumbnail"] = thumbs[pic]
            found = True
    if not found:
        # create new entry
        old_gallery.append(
            {"filename": pic, "sizes": gallery[pic], "thumbnail": thumbs[pic], "original": originals[pic]})

# check if path existing
if "picture_folder" not in input_gallery:
    input_gallery["picture_folder"] = '/'.join(folder_names)

# write to output file
print('Writing YAML data to file...')
with open(output_file, 'w') as f:
    f.write(yaml.dump(input_gallery, default_flow_style=False))
