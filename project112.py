import os
import shutil

from_dir = "C:/Users/Ethan/Desktop/"
to_dir = "C:/Users/Ethan/Downloads/"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for filename in list_of_files:
    name, extension = os.path.splitext(filename)
    print(name)
    print(extension)