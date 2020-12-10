def day10p2():
    inFile = open("files/day10.txt", 'r')
    joltages = []
    diff1 = 1 #initial outlet difference
    diff3 = 1 #final adapter difference
    for line in inFile:
        joltages += [int(line)]
    joltages += [0] #needed for all paths (2 could come from 1 or straight from 0)
    joltages.sort()
    joltages.reverse()
    tree = buildTree(joltages)
    return treePathCount(tree)

def buildTree(sortedL):
    rValue = sortedL[0]
    r = node(rValue)
    buildHelper(r, sortedL)
    return r

def buildHelper(n, sL): #takes a node and a sortedList
    v = n.value
    d3 = v - 3
    d2 = v - 2
    d1 = v - 1
    check = 1 #could make separate check function
    sLength = len(sL)
    if check < sLength and sL[check] == d1:
        n.diff1 = node(d1)
        buildHelper(n.diff1, sL[check:])
        check += 1
    if check < sLength and sL[check] == d2:
        n.diff2 = node(d2)
        buildHelper(n.diff2, sL[check:])
        check += 1
    if check < sLength and sL[check] == d3:
        n.diff3 = node(d3)
        buildHelper(n.diff3, sL[check:])

def treePathCount(root):
    while root != None:
        if root.diff1 == root.diff2 == root.diff3 == None: #found starting point
            return 1
        s1 = treePathCount(root.diff1)
        s2 = treePathCount(root.diff2)
        s3 = treePathCount(root.diff3)        
        return s1 + s2 + s3
    return 0
class node():
    def __init__(self, value): #node with three branches
        self.value = value
        self.diff3 = None
        self.diff2 = None
        self.diff1 = None
    
    def __str__(self): #used for debugging
        return str(self.value) +" - " + "diff3: " + str(self.diff3) + "  diff2: " + str(self.diff2) + "  diff1: " + str(self.diff1)

def main():
    print("Total: " + str(day10p2()))

if __name__ == "__main__":
    main()
