#Read files
import os


"""import os
print (os.getcwd(demofile.txt))
"""




"""
path = "python3.7 ~/Desktop/Python/demofile.txt"
f = open(path)
f.write("Hello world")
f.close()
#"""

f = open("demofile.txt", "r")
print(f.read())
