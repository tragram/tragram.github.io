import os
from datetime import datetime

folder_name = 'D:/tragram.github.io/assets/img/03-riga/gallery'
dir_list = [os.path.join(folder_name, x) for x in os.listdir(folder_name)]
JPG_timezone_correction=-1
for file in dir_list:
    # print(file)
    filename, file_extension = os.path.splitext(file)
    date = datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y_%m_%d_%H_%M_%S')
    if file_extension==".JPG":
        date=date[:11]+str(int(date[11:13])+JPG_timezone_correction)+date[13:]
    try:
        os.rename(file, os.path.join(folder_name, date + file_extension))
    except Exception as e:
        print(e)
print(os.listdir(folder_name))