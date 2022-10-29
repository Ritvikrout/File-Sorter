from distutils import extension
import os
import shutil

from_dir = "/Users/satya/Downloads"

to_dir = "/Users/satya/Downloads"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files :
    name,ext = os.path.splitext(file_name)
    print(name)
    print(ext)
    if ext == ' ' :
        continue
    if ext in ['.doc', '.docx', '.rtf', '.txt', '.pdf'] :
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + 'Document_Files'
        path3 = to_dir + '/' + 'Document_Files' + '/' + file_name
        print('moving from', path1)
        print('moving to', path3)
        if os.path.exists(path2) :
            print("Moving", file_name, "to", path2, '  .....')
            shutil.move(path1, path2)
        else : 
            os.mkdir(path2)
            print("Moving", file_name, "to", path2, '  ......')
            shutil.move(path1, path2)