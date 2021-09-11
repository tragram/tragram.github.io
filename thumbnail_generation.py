import sys
from os import listdir
from os.path import isfile, join
from PIL import Image, ImageOps
import pathlib

# configuration
THUMBNAIL_SIZE=1000
try:
    path = sys.argv[1]
except:
    print("You need to provide folder as an argument!")
    quit()

extensions = ['jpg', 'png', "JPG", "jpeg"]
folder_names = [pathlib.PurePath(path).name]
print(folder_names)
# extract image files
print('Collecting files...')
files = [f for f in listdir(path) if isfile(join(path, f))]
files = [f for f in files if f[f.rfind('.')+1:] in extensions]
# don't change previously generated files
files = [f for f in files if "--" not in f]
print(files)
for f in files:
    image_name = f[:f.rfind('.')]
    img = Image.open("./assets/img/"+'/'.join(folder_names)+"/"+f)
    img = ImageOps.exif_transpose(img)
    img.thumbnail([THUMBNAIL_SIZE, THUMBNAIL_SIZE])
    filename = "thumbnail--" + image_name +  f[f.rfind('.'):]
    img.save("./assets/img/"+'/'.join(folder_names)+"/"+filename)

