## Nathan Burwig
## AoC Day 3 Challenge
## 12/3/2022
## Bugs: None noted, but the code is far from optimized, just a quick solution
## Purpose:
##      This challenge was to identify letters in common between sets of
##      strings. In the first part, we split a string in half, find the common
##      letter between them. In part 2 we find the common letter in a set of
##      three lines

## https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r")       #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

## * I/O Prepper
def function(arr):
    # line = arr[0]
    for thing in arr:
        print(thing.split(","))
        
## get input file
arr = readFile("input_files/input3")



##      Start Problem 1     ##
## converts character into associated proprity
def priority(ch):
    if ch.isupper():
        return ord(ch) - 38
    elif ch.islower():
        return ord(ch) - 96

# finds common char between the two halves, calculates and sums priority values
x = 0
for j in arr:
    ## from https://stackoverflow.com/questions/4789601/split-a-string-into-2-in-python
    comp1, comp2 = j[:len(j)//2], j[len(j)//2:]
    for i in comp1:
        if i in comp2:
            x = x + priority(i)
            break

print("part 1:", x)


##      Start Problem 2     ##
# iterate through three at a time and find common values in sets of three
x, i = 0, 0
while i < 300:
    curr = [arr[j] for j in range(i, i + 3)]
    for k in curr[0]:
        if k in curr[1] and k in curr[2]:
            x = x + priority(k)
            break
    i = i + 3

print("part 2:", x)
