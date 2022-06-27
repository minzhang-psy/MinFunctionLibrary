'''
Title: Demographic
Author: Min Zhang
-----------------
# Function to copy files from subfolders into one folder
'''


import os
import shutil

def multiCopy():
    src_path = input("Please enter your source path:\n")   #source path (main folder)
    out_path = input("Please enter your destination path:\n") # destination path
    end_pattern = input("Please enter filename ending patter:\n") #patern of moving filename

    #print(src_path, out_path, end_pattern)
    for dirpath, dirnames, filenames in os.walk(src_path):
        for filename in filenames:
            if filename.endswith(end_pattern):
                src = os.path.join(dirpath, filename)
                dest = os.path.join(out_path, filename)
                #print(dirpath)
                shutil.copy2(src,dest)
                           
    


                 
