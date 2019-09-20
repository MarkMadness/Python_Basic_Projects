#
#       Drill 1 from Python Course
#
#       Mark Roenfeldt
#
#       Write a script that will check a specific folder on the hard drive, verify whether those files
#           end with a “.txt” file extension and if they do, print those qualifying file names and
#           their corresponding modified time-stamps to the console.
#----------------------------------------------------------------------------------------------------------------------------------------------
#       use the listdir() method from the OS module to iterate through all files within a specific directory 
#
#       use the path.join() method from the OS module to concatenate the file name to its file path, forming an absolute path.
#
#       use the getmtime() method from the OS module to find the latest date that each text file has been created or modified.
#
#       print each file ending with a “.txt” file extension and its corresponding mtime to the console
#----------------------------------------------------------------------------------------------------------------------------------------------
#       create a new directory on your system and then create 10 different files within this folder. The files that you create should be
#           a combination of any file types you would like just as long as you include at least two that are text documents ending with a
#           “.txt” file extension.


import os
import time

FilePath = '/Users/markroenfeldt/Desktop/Tech Academy/Projects/Python/Drill_1/'

dirFiles = os.listdir(FilePath)

#print('     All the files in the directory...')
for file in dirFiles:
    ext = os.path.splitext(file)[-1].lower()
    #   [For Testing]   print(file)
    if ext == ('.txt'):
        print('A file with .txt extention: ' + file)
        cPath = os.path.join(FilePath, file)
        #   [For Testing]   print(cPath)
        mod_time = os.path.getmtime(cPath) 
        #   [For Testing]   print("Latest modification on directory: ", mod_time)
        local_time = time.ctime(mod_time) 
        print("   Last time of modification:", local_time)
