import sys
import os
from datetime import datetime
import pathlib
from PIL import Image

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
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
files = [f for f in files if f[f.rfind('.')+1:] in extensions]

JPG_timezone_correction=-1
folder_name=path+'\\'
for file in files:
    # print(file)
    filename, file_extension = os.path.splitext(file)
    time_taken=Image.open(folder_name+file).getexif().get(306)
    if time_taken is None:
        continue
    date = datetime.strptime(time_taken,'%Y:%m:%d %H:%M:%S').strftime('%Y_%m_%d_%H_%M_%S')
    if file_extension==".JPG":
        date=date[:11]+str(int(date[11:13])+JPG_timezone_correction)+date[13:]
    try:
        os.rename(folder_name+file, os.path.join(folder_name, date + file_extension))
    except Exception as e:
        print(e)
print(os.listdir(folder_name))