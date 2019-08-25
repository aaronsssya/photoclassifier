#!python3
import os
import re
import shutil

from PIL import Image
from datetime import datetime

def get_date_taken(path):
    return Image.open(path)._getexif()[36867]

# Photo folder
def copy_photo(source, destination):
    if source:
        None
    else:
        source = '~/Pictures/Photos Library.photoslibrary/Masters'
    for folder, sub_folders, files in os.walk(source):
        for file in files:
            try:
                datetme_obj = datetime.strptime(get_date_taken(folder+'/'+file), '%Y:%m:%d %H:%M:%S')
                des_folder = datetime.strftime(datetme_obj, '%Y%m%d')
            except:
                des_folder = 'video'
            if os.path.exists(destination+'/'+des_folder):
                None
            else:
                os.makedirs(destination+'/'+des_folder)
            if os.path.exists(destination+'/'+des_folder+'/'+file):
                print(des_folder+'/'+file,'is existing')
            else:
                print('copy',str(folder)+'/'+str(file), 'to', str(destination)+'/'+str(des_folder))
                shutil.copy(folder+'/'+file, destination+'/'+des_folder)

if __name__ == '__main__':
    source = input("type source path: ")
    destination = input("type destination pth: ")
    copy_photo(source, destination)