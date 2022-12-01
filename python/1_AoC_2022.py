## Nathan Burwig
## AoC Day 1 Challenge
## 12/1/2022
## Purpose:
##      The first challenge in the 2022 Advent of Code challenge. This problem was
##      to take in a data separated by empty lines. Each chunk of data represented
##      information to be summed. The challend was then to find the chunk that
##      summed to the highest value, then the top three highest values. What follows is
##      my solution.

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
arr = readFile("input_files/input1")

## Sum calories for each elf and put into elves array
elves = []
sum = 0
for i in range(len(arr)):
    if arr[i] == '':
        elves.append(sum)
        sum = 0
    else:
        sum = int(arr[i]) + sum
        
## find max values of top three elves
max1 = max(elves)
elves.remove(max1)

max2 = max(elves)
elves.remove(max2)

max3 = max(elves)

## print relevant data (solution)
print("Max calories carried by elf:", max1)
print("Calories carried by top three elves:", max1 + max2 + max3)
