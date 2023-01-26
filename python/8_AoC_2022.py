## Nathan Burwig
## AoC Day 6 Challenge
## 12/6/2022
## Bugs: None noted, but the code is far from optimized, just a quick solution
## Purpose: 
##      Finds the first occurence of a unique string (no repeating chars)
##      of size win_len. See function description below in "HELPFUL FUNCTIONS"


## https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r")       #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

## * I/O Prepper
def function(arr):
    for thing in arr:
        print(thing.split(","))
        
## get input file
arr = readFile("input_files/input7")


##     PREPROCESS DATA      ##



##      HELPFUL FUNCTIONS   ##




##      Start Problem 1     ##
##      Start Problem 2     ##

