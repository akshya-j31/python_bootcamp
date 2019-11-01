import os
import os.path
from os import path

def main():
    FileName = input("Please enter the file name: ")
    if path.exists(FileName):
        print("file exists")
        UserInput = input("***Please enter your choice***\na. Read the file\nb. Delete the file and start over\nc. Append the file\n\n")
        if UserInput == 'a':
            f = open(FileName,"r")
            print(f.read())
        elif UserInput == 'b':
            os.remove(FileName)
            f = open(FileName,"w+")
            f.write("")
        elif UserInput == 'c':
            FileTxtAppend = input("Please enter the text to append:\n")
            f = open(FileName,"a")
            f.write(FileTxtAppend)
        else:
            print("Wrong choice")
    else:
        FileTxt = input("File does not exist. Please enter the text which you want to write:\n")
        f = open(FileName,"w+")
        f.write(FileTxt)

if __name__== "__main__" :
    main()