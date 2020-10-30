import os


def  delete_files(folder_path):
    # dirs="D:/python_work/identify/image"
    dirs=folder_path
    # dirs=path_str
    myList=os.listdir(dirs)
    for i in myList:
        file_path=folder_path+"/"+i
        os.remove(file_path)

folder_path="D:/test"
delete_files(folder_path)