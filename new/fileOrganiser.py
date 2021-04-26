import os
import shutil
path = input("enter the name of the directory to be sorted: ")
listOfFiles = os.listdir(path)

# To go through each and every file
for file in listOfFiles:
    name,ext = os.path.splitext(file)

    #To force the next iteration (and store the extension type)
    ext = ext[1:]

    #if it is a directory (empty extension)
    if ext=="":
        continue
    
    # To move the directory where "ext" exists
    if os.path.exists(path + '\\' + ext):
        shutil.move(path + '\\' + file, path+'\\'+ext+'\\'+file)

    #To create a new directory if "ext" does not exist
    else:
        os.makedirs(path+'\\'+ext)
        shutil.move(path+'\\', path+'\\'+ext+'\\'+file)
        