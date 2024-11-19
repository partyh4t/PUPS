
# unneeded file detector/deleter

import os, sys
from pathlib import Path

path_name = r'C:\Users\ray\OneDrive\Desktop\Temporary\python_scripts\ATBS'

def fileSize(path):
    big_files = {}
    for roots, dirs, files in os.walk(path):
        base_name = os.path.basename(path)
        #print('\nCurrent directory: "' + roots + '"')
        for file in files:
            size = os.path.getsize(os.path.join(roots, file))
            if size > 1000:
                big_files[file] = size
                #print(f'Deleting {file}!')
                #os.unlink(os.path.join(roots, file)) DELETES FILE
            '''
            relative_dir = os.path.relpath(roots, path)
            if relative_dir == '.':
                print(os.path.join(base_name, file) + ': ' + str(size))
            else:
                print(os.path.join(base_name, relative_dir, file) + ': ' + str(size))
            '''
        #print()
    return big_files

big_files = fileSize(path_name)
for i, j in big_files.items():
    print(f'I could have deleted the "{i}" file! It takes up {j} Bytes of space currently.')