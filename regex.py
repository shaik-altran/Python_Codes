import re
import os

def MAINTAINERSDIRpathfromuboot(Filetobesearched,searchfrom):
    paths = []

    for root,dir,exactfile in os.walk(searchfrom):
        if Filetobesearched in exactfile:
            paths.append(os.path.join(root, Filetobesearched))

    return paths


searchfrom = r'/home/shaik/u-boot_latest'
Filetobesearched = "MAINTAINERS"
pattern = r'[M|R]:[\s]([\w\s\.\-:]+)[\s]<([\w\.\-\+]+)@([\w\.\-]+)>'
userdata = []
infoinfile = []

paths = MAINTAINERSDIRpathfromuboot(Filetobesearched,searchfrom)

for path in paths:
    file = open(path,'r')
    infoinfile = file.read()
    file.close()
    for match in re.finditer(pattern,infoinfile):
        userdata.append(match.groups())
    textfile = open("userdata.txt","a")
    textfile.write(path + '\n')
    for data in userdata:
        for info in data:
            textfile.write(info + '\n')

    textfile.close()
                
    
"""textfile = open("userdata.txt","a")

for data in userdata:
    for info in data:
        textfile.write(info + '\n')

textfile.close()


""" 


