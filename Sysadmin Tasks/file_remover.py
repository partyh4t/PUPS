
# oversized file remover

# this script can be used to detect (or delete if preferred) all files over a certain given size.

import os

path_name = r'C:\Users\Zayd\Desktop\Coding'

def fileSize(path):
    big_files = {}
    for roots, dirs, files in os.walk(path):
        base_name = os.path.basename(path)
        for file in files:
            size = os.path.getsize(os.path.join(roots, file))
            if size > 1000: #change this to configure how large a file should be in bytes to be detected
                big_files[file] = size
                relative_dir = os.path.relpath(roots, path)
                if relative_dir == '.':
                    print(os.path.join(base_name, file) + ': ' + str(size) + ' bytes')
                else:
                    print(os.path.join(base_name, relative_dir, file) + ': ' + str(size) + ' bytes')
                deleteFile(file)
                print()
    return big_files

def deleteFile(file):
    print(f'Deleting {file}!')
    #os.unlink(os.path.join(roots, file)) --- DELETES FILES

fileSize(path_name)


