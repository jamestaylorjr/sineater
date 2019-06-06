
import pandas
import os 
from os.path import isfile, join


def getDirtyLines():
    dirtyLines = []
    mypath = '.'
    pathlist = os.listdir(mypath)
    files = [f for f in pathlist if isfile(join(mypath, f))]
    counter = 0
    while counter < len(files):
        print(files[counter])
        if files[counter] == "Dirty1.txt":
            with open(files[counter]) as f: 
                for line in f:
                    counter2 = 0
                    counter3 = 0
                    while counter2 < len(line):
                        if counter2 > 7:
                            if (line[counter2-1] + line[counter2]) == ". ":
                                if line[counter2-3] + line[counter2-2] + line[counter2-1] != " [A-Z].":
                                    #print(line[counter2:])
                                    dirtyLines.append(line[counter3:counter2])
                                    counter3 = counter2
                        counter2+=1
        counter+=1
    #print(dirtyLines)
    return(dirtyLines)

def getCleanLines():
    cleanLines = []
    mypath = '.'
    pathlist = os.listdir(mypath)
    files = [f for f in pathlist if isfile(join(mypath, f))]
    counter = 0
    while counter < len(files):
        print(files[counter])
        if files[counter] == "Clean1.txt":
            with open(files[counter]) as f: 
                for line in f:
                    counter2 = 0
                    counter3 = 0
                    while counter2 < len(line):
                        if counter2 > 10:
                            if (line[counter2-1] + line[counter2]) == ". ":
                                if line[counter2-3] + line[counter2-2] + line[counter2-1] != " [A-Z].":
                                    #print(line[counter2:])
                                    cleanLines.append(line[counter3:counter2])
                                    counter3 = counter2
                        counter2+=1
        counter+=1
    #print(cleanLines)
    return(cleanLines)


def main():
    dirty = getDirtyLines()
    clean = getCleanLines()

    print(dirty)
    print(clean)

    lengthdiff = len(dirty) - len(clean)
    additioncounter = 0

    while additioncounter < lengthdiff:
        clean.append("n/a")
        additioncounter+=1

    df = pandas.DataFrame(data={"dirty_lines": dirty, "clean_lines": clean})
    df.to_csv("./sineatertest1.csv", sep=',',index=False)
    

main()

