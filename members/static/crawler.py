import os

path = r'./OG/Mundu Basketball'

for folders,x, files in os.walk(path):
    for count,f in enumerate(files):
        print(folders+"/"+f,folders+"/"+str(count+1)+".JPG")
        os.rename(folders+"/"+f,folders+"/"+str(count+1)+".JPG")
