import re
import sys

try:
    f = open(sys.argv[1], "r")
except:
    sys.exit("ERROR:Arguments not sufficent or typo error in argument")

data = f.read()

pattern = r'[^#include<|"]\w+.h|.dtsi'

match = re.findall(pattern,data)

print(match)





