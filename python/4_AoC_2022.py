## Nathan Burwig
## AoC Day 4 Challenge
## 12/4/2022
## Bugs: None noted, but the code is far from optimized, just a quick solution
## Purpose:
##      This challenge was to find if different ranges of numbers are
##      completely contained in one another, or (in part 2) if there is any 
##      overlap at all

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
arr = readFile("input_files/input4")



##      Start Problem 1     ##
## fills out values between the two integers given in the data and returns that
## as a set
def fill(a):
    b = a.split('-')
    lst = [i for i in range(int(b[0]), int(b[1]) + 1)]
    return set(lst)

# counts the number of set pairs which are completely contained in eachother
count = 0
for i in arr:
    a = fill(i.split(',')[0])
    b = fill(i.split(',')[1])
    if a.issubset(b) or b.issubset(a):
        count += 1

print("part 1:", count)


##      Start Problem 2     ##
# counts number of sets with a nonzero intersection
count = 0
for i in arr:
    a = fill(i.split(',')[0])
    b = fill(i.split(',')[1])
    if a.intersection(b):
        count += 1

print("part 2:", count)
