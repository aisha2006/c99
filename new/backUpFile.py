import os
import shutil

source = input("enter source: ")
destination = input("enter destination")

source = source+"\\"
destination = destination+"\\"

listOfFiles = os.listdir(source)

for file in listOfFiles:
    shutil.copy((source+file),destination)