import os
from datetime import datetime

folder_name = 'D:/tragram.github.io/assets/img/01-varsava/gallery'
dir_list = [os.path.join(folder_name, x) for x in os.listdir(folder_name)]

for file in dir_list:
    # print(file)
    filename, file_extension = os.path.splitext(file)
    date = datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y_%m_%d_%H_%M_%S')
    try:
        os.rename(file, os.path.join(folder_name,date + file_extension))
    except Exception as e:
        print(e)
print(os.listdir(folder_name))