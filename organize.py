import os
import shutil
from_dir = "C:/Users/salma/Downloads/New folder (3)/C102_assets-main"
to_dir = "C:/Users/salma/Desktop/Class102"
listOfFiles = os.listdir(from_dir)


for fileName in listOfFiles:
    name,extension = os.path.splitext(fileName)
    if extension == "":
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        path1 = from_dir + "/" + fileName
        path2 = to_dir + "/" + "Image_Files"
        path3 = to_dir + "/" + "Image_Files" + "/" + fileName

    if os.path.exists(path2):
        print("Moving " + fileName + ".....")
        shutil.move(path1,path3)

    else:
        os.makedirs(path2)
        print("Moving " + fileName + ".....")
        shutil.move(path1,path3)
