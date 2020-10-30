import os

dirPath=os.getcwd()
filePath='delicious'
fileAbaPath=os.path.join(dirPath,filePath)

for filename,subfolders,subfiles in os.walk(fileAbaPath):
    print(filename)

    for subfolder in subfolders:
        print(filename+' ‘s subfolder is:'+subfolder)

    for subfile in subfiles:
        print(filename+' ‘s subfile is:'+subfile)
