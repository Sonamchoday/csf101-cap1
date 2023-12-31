import os
import shutil

downloads_folder = os.path.expanduser("~/Downloads")
images_folder = os.path.expanduser("~/Documents/Images")

if not os.path.exists(images_folder):
    os.makedirs(images_folder)

for file_name in os.listdir(downloads_folder):
    if file_name.endswith(".PNG") or file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
        file_path = os.path.join(downloads_folder, file_name)
        shutil.move(file_path, images_folder)
