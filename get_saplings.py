import os

def doit():
    trees = []
    dir = "D:\Prosjekter\Minecraft\Trees"
    outputString = ""
    count = 0
    for subdir, dirs, files in os.walk(dir):
        for file in files:
            tree = file[:-4]
            type = subdir.replace(dir+"\\", "")
            if type not in trees:
                trees.append(type)
                count = len(files)
                if len(outputString):
                    print(outputString[:-1] + ")")
                outputString = "Sapling(" + type + ","
            outputString += tree + "," + str(round(100 / count)) + ","
            count -= 1
    print(outputString[:-1] + ")")
doit()
