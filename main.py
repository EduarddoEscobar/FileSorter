import shutil
import pathlib
from os import listdir, mkdir
from os.path import isfile, join, exists

myPath = input("Enter file location: ")

#Gets all the files in the folder
files = [f for f in listdir(myPath) if isfile(join(myPath, f))]

for f in files:

    #Path of file
    filePath = myPath+'\\'+f

    #Gets the type of file
    suffix = pathlib.Path(filePath).suffix
    suffix = suffix[1:]

    folderPath = myPath+'\\'+suffix

    #Checks if there is already a folder
    if not exists(folderPath):
        mkdir(folderPath)
        print("Directory ", folderPath, " Created ")

    #Puts file in a folder
    copyPath = folderPath+'\\'+f
    shutil.move(filePath, copyPath)
    print(suffix)
