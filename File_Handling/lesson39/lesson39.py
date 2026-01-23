#binary mod can't get a encoding

with open("File_Handling/lesson39/2.png","rb") as f:
    print(f.read())


#now we want delete this png

import os
#if there is file
if os.path.exists("File_Handling/lesson39/2.png"):
    os.remove("File_Handling/lesson39/2.png") #remove it
else:
    print("This file not exist")

#for creating and removing empty folders
print(os.listdir()) #list all of files and folders

#Create new foler with that path  carefull about \ 
os.mkdir("C:\\Users\\abc13\\OneDrive\\Masaüstü\\python-learning\\File_Handling\\lesson39\\emptyfolder")

#remove that folder
os.rmdir("File_Handling/lesson39/emptyfolder")