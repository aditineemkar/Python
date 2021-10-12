import os
import shutil

# path=input("Enter the path:- ")
# listOfFiles=os.listdir(path)
# for i in listOfFiles:
#     name, ext=os.path.splitext(i)
#     ext=ext[1:]
#     if ext=="":
#         continue
#     if os.path.exists(path+"/"+ext):
#         shutil.move(path+ '/'+i, path+"/"+ext+"/"+i)
#     else:
#         os.mkdir(path+"/"+ext)
#         shutil.move(path+ "/"+i, path+"/"+ext+'/'+i)

source = input("Enter the source:- ")
destination= input("Enter the destination:- ")
source = source+"/"
destination=destination+"/"
listOfFiles = os.listdir(source)
for i in listOfFiles:
    shutil.copy((source+i), destination)
