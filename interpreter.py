import sys
import pathlib
from core import *
lang_name = sys.argv[1]
file_name = sys.argv[2]
#if sys.argv[0] != "cy"
if lang_name == "cy":
    file = pathlib.Path(file_name)
    if file.exists ():
        #print ("File exist")
        content = open(file,'r')
        data = content.read()
        data = data.strip()
        find_variable(data)
        println(data)
        content.close()
    else:
        println("File Does not exist")
        open(file, 'a')
        println(f"Created new file {file}")
