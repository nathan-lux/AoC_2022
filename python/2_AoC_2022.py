## Nathan Burwig
## AoC Day 2 Challenge
## 12/2/2022
## Bugs: None noted, but the code is far from optimized, just a quick solution
## Purpose:
##      The idea behind this challenge is to play rock paper scissors. In
##      problem one, ABC are computer moves and XYZ are our moves, all from the
##      input file. In part 2, we take XYZ to be win lose or draw (not in
##      order) then determine the overall points based on what our opponent
##      plays.

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
        
## a function that does something split already does but this makes my life
## easier bc it's two lines and i never remember the syntax for splits :)
def concat(a):
    return a[0] + a[1]

## get input file
arr = readFile("input_files/input2")


##      Start Problem 1     ##
# dictionaries to help determine the outcomes of the game
# points for win/draw plus points for hand played
points = {
        "rock":     1,
        "paper":    2,
        "scissors": 3,
        "AY": 6,
        "BZ": 6,
        "CX": 6,
        "AX": 3,
        "BY": 3,
        "CZ": 3
        }
play = {
        'X': "rock",
        'Y': "paper",
        'Z': "scissors"
        }
comp = {
        'A': "rock",
        'B': "paper",
        'C': "scissors"
       }

# keep track of points
total = 0

# loop through and figure out how the games turn out
for i in arr:
    curr = i.split()

    s = concat(curr)
    c = curr[0]
    p = curr[1]

    # poitns for hand played
    total += points[play[p]]

    # points for win lose or draw
    try:
        total += points[s]
    except:
        points = points

print("part 1:", total)


##      Start Problem 2     ##
# more dictionaries for determine move based off computers move
lose = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
       }
win = {
        "rock": "paper",
        "paper": "scissors",
        "scissors": "rock"
       }

LOSE = 'X'
DRAW = 'Y'
WIN  = 'Z'

total = 0

# similar loop setup, but with win lose or draw cases separately
for i in arr:
    curr = i.split()
    print(curr)

    c = curr[0]
    p = curr[1]

    if p == LOSE:
        total = total + points[lose[comp[c]]] + 0
        print("lose")
    elif p == WIN:
        total = total + points[win[comp[c]]] + 6
        print("win")
    elif p == DRAW:
        print("draw")
        total = total + points[comp[c]] + 3

print("part 2:", total)





