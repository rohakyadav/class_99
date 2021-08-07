import os 
import shutil
source = input("enter source folder name :: ")
destination = input("enter destination folder name :: ")
source = source + '/'
destination = destination + '/'
# write the name of the directory that needs to get sorted 
# path = 'C:\Users\Rohak\Downloads\whitehat_coding\class_99'
#path = '/home/User/Desktop/file.txt' # Split the path in 
# root and ext pair root_ext = os.path.splitext(path) 
# print root and ext 
#  of the specified path print("root part ", root_ext[0]) print("ext part " , root_ext[1], "\n")
path = input('enter the name of the directory to be sorted')
list_of_file = os.listdir(path)
for file in list_of_file:
    name,ext = os.path.splitext(file)
    ext = ext[1]
    if ext == '':
        continue


    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
