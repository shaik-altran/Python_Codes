import re


pattern = r'\#include[\s]*[<|"]([\w\.\-\/]+)[>|"]'

path = input("Please enter the path of a file to search for: ")

file = open(path, 'r')

filedata = file.read()

headerfiles = re.findall(pattern, filedata)

for headerfile in headerfiles:
    print(headerfile)


