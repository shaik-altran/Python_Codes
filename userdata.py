import re
import os
import json

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
Dictionary = {}

paths = MAINTAINERSDIRpathfromuboot(Filetobesearched,searchfrom)

for path in paths:
    file = open(path,'r')
    infoinfile = file.read()
    file.close()
    for match in re.finditer(pattern,infoinfile):
        userdata.append(match.groups())
    jsonfile = open('userdata.json','a')
    jsonfile.write(path + '\n\n')
    for data in userdata:
        for i in range(0,len(data),3):
            Dictionary.update({'UserName' : data[i]})
            Dictionary.update({'User_ID' : data[i+1]})
            Dictionary.update({'Domain'   : data[i+2]})
            json_Object = json.dumps(Dictionary)
            jsonfile.write(json_Object+'\n')
    jsonfile.close()
            
        


