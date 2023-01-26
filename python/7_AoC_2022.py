## Nathan Burwig
## AoC Day 6 Challenge
## 12/6/2022
## Bugs: None noted, but the code is far from optimized, just a quick solution
## Purpose: 
##      Finds the first occurence of a unique string (no repeating chars)
##      of size win_len. See function description below in "HELPFUL FUNCTIONS"

from treelib import Node, Tree

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
cd = "$ cd"
ls = "$ ls"
dots = ".."
di = "dir"
curr_root = "/"

tree = Tree()
tree.create_node("/", "/")

for j in range(len(arr)):
    line = arr[j]
    if cd in line and not dots in line:
        cmdlet = line.split()
        curr_root = cmdlet[2]
        #print("found cd:", curr_root)

    if ls in line:
        #print("found ls")

        for i in range(j + 1, len(arr) - 1):
            curr = arr[i].split()
            #print("\t", curr)

            if curr[0] == di:
                try:
                    tree.create_node(curr[1], curr[1], parent = curr_root)
                    #print("\t\t adding", curr[1], "to", curr_root)
                except:
                    pass
            elif curr[0].isdigit():
                try:
                    tree.create_node(curr[0], curr[1], parent = curr_root)
                    #print("\t\t adding", curr[1], "to", curr_root)
                except:
                    pass
            if cd in arr[i + 1]:
                 break
tree.show()
print(tree.WIDTH)
##      Start Problem 2     ##

#for j in range(len(arr)):
#    line = arr[j]
#    if cd in line and not dots in line:
#        #print(line)
#        curr_dir = line.split()[2]
#        tree[curr_dir] = []
#    elif ls in line:
#        #print(line, curr_dir)
#        for i in arr[j + 1:len(arr)]:
#            #print("\t", i)
#            if cd in i:
#                break
#            else:
#                tree[curr_dir].append(i)
#                
#def compute_size(lst):
#    size = 0
#    for i in lst.split():
#        if i.isdigit():
#            size += int(i)
#    return size
##def comp_dir_size(dr):
#
#
#            
#for x in tree:
#    size = 0        
#    for i in tree[x]:
#        size += compute_size(i)
#    tree[x].append(size)
#
#for x in tree:
#    for i in tree[x]:
#        try:
#            if di in i:
#                tree[x][-1] += tree[i.split()[1]][-1]
#        except Exception as e:
#            pass
#pprint.pprint(tree)
#
#sum = 0
#for x in tree:
#    if tree[x][-1] <= 100000:
#        sum += tree[x][-1]
#print(sum)
##      Start Problem 2     ##

