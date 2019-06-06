
import pandas
import os 
from os.path import isfile, join


def getDirtyLines():
    """
    Gets lines from unedited manuscript(s)
    """
    dirtyLines = []
    mypath = './sineater/' #I changed this based on my filestructure. It can be whatever -- Jim
    pathlist = os.listdir(mypath)
    #check that items are actually text files
    files = [f for f in pathlist if isfile(join(mypath, f)) and '.txt' in f]
    for file in files:
        print(file)
        #only select files with dirty in the filename
        if 'dirty' in file.lower():
            with open(mypath+file, 'r') as f: 
                for line in f:
                    line = line.strip('\n')
                    for item in line.split('. '):
                        if item != '':
                            dirtyLines.append(item)
    return(dirtyLines)

def getCleanLines():
    """
    Gets lines from edited manuscript(s)
    """
    cleanLines = []
    mypath = './sineater/' #I changed this based on my filestructure. It can be whatever -- Jim
    pathlist = os.listdir(mypath)
    #check that items are actually text files
    files = [f for f in pathlist if isfile(join(mypath, f)) and '.txt' in f]
    for file in files:
        print(file)
        #only select files with clean in the filename
        if 'clean' in file.lower():
            with open(mypath+file, 'r') as f: 
                for line in f:
                    line = line.strip('\n')
                    for item in line.split('. '):
                        if item != '':
                            cleanLines.append(item)
    return(cleanLines)

#this does the same thing as setting the main function in other languages
if __name__ == "__main__":
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
    df.to_csv("./sineatertest2.csv", sep=',',index=False)
    
