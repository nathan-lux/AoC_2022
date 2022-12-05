## Nathan Burwig
## AoC Day 5 Challenge
## 12/5/2022
## Bugs: None noted, but the code is far from optimized, just a quick solution
## Purpose:
##      This challenge was to move crates around based on input movements. The
##      crates are stacked atop one another, so moving them was akin to just popping
##      and pushing from a stack. I wasn't familiar with python deque and collections,
##      so i just did it manually. The data is of the form seen below.
## DATA:
##      [T]     [Q]             [S]
##      [R]     [M]             [L] [V] [G]
##      [D] [V] [V]             [Q] [N] [C]
##      [H] [T] [S] [C]         [V] [D] [Z]
##      [Q] [J] [D] [M]     [Z] [C] [M] [F]
##      [N] [B] [H] [N] [B] [W] [N] [J] [M]
##      [P] [G] [R] [Z] [Z] [C] [Z] [G] [P]
##      [B] [W] [N] [P] [D] [V] [G] [L] [T]
##       1   2   3   4   5   6   7   8   9
##      
##      move 5 from 4 to 9
##      move 3 from 5 to 1
##      ...


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
arr = readFile("input_files/input5")


##          HELPFUL FUNCTIONS        ##
## get the row number for the column numbers in the stacks.
def find_index_row(lst):
    n_row = 0
    for i in arr:
        curr = i.split()
        if str(1) in curr and str(2) in curr:
            n_row = arr.index(i)
            return n_row

## gets the stacks from the indices of the column numbers in data
def get_stacks(indices, lst):
    cols = []
    for i in indices:
        lst = []
        for j in range(0, n_row):
            if arr[j][i] != ' ':
                lst.append(arr[j][i])
        cols.append(lst)
    return cols

## parses move set data from a sliced portion of the original input
def parse_moves(lst):
    ins = []
    for i in lst:
        tup = []
        for j in i.split():
            if j.isdigit():
                tup.append(int(j))
        ins.append(tup)
    return ins

## prints the solution in a nice way
def print_sol(cols, part):
    sol = []
    for i in cols:
        sol.append(i[0])
    print("part", str(part) + ':', sol)



##      PREPROCESS DATA     ##
# find row of column numbers and get indices from that row
n_row = find_index_row(arr)
inds = [arr[n_row].index(str(i)) for i in range(1, 10)]

# initialize the stacks for both parts of the challenge
cols_p1 = get_stacks(inds, arr)
cols_p2 = get_stacks(inds, arr)

# get input moves
ins = parse_moves(arr[n_row + 2:])


##      Start Problem 1     ##
# execute commands given in inputs
for i in ins:
    move  = i[0]
    fromm = i[1] - 1
    to    = i[2] - 1
    for j in range(0, move):
        curr = cols_p1[fromm]
        cols_p1[to].insert(0, curr[0])
        cols_p1[fromm].remove(curr[0])

print_sol(cols_p1, 1)


##      Start Problem 2     ##
for i in ins:
    move  = i[0]
    fromm = i[1] - 1
    to    = i[2] - 1

    m = cols_p2[fromm][0:move]

    for i in range(0, move):
        cols_p2[to].insert(0, m[move - i - 1])
        cols_p2[fromm].remove(m[move - i - 1])

print_sol(cols_p2, 2)
