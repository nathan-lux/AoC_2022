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
arr = readFile("input_files/input6")


##      PREPROCESS DATA     ##
stream = "".join(arr)


##          HELPFUL FUNCTIONS        ##
## name:    window_search
## param:   win_len -- length of window to scan for unique chars in
## returns: ans     -- index of first unique string + win_len
## purpose: scans window of length win_len for strings containg no two chars of
##          the same type (ie window cannot have to 'n's in it)
def window_search(win_len):
    # loop through starting at the length of the first window
    for i in range(win_len - 1, len(stream)):
        window = []
    
        # get all the characters in a given window
        for j in range(0, win_len):
            window.insert(0, stream[i-j])
    
        # check if all characters are unique via set conversion
        if len(set(window)) == win_len:
            key = window
            break
    
    # calculate and return solution (index of first string + win_len)
    ans = stream.index("".join(key)) + win_len
    return ans


##      Start Problem 1     ##
print("part 1:", window_search(4))        


##      Start Problem 2     ##
print("part 2:", window_search(14))

