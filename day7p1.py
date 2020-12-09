def day7p1():
    total = 0 
    inFile = open("files/day7.txt", 'r')
    groups = []
    str = ""
    for line in inFile:
        str += line
    bagRules = str.split('\n')
    dict = {}
    for bag in bagRules: #bag is a string
        b = bag.split()
        name = b[0] + " " + b[1]
        rules = b[4:]
        rules = " ".join(rules)
        dict[name] = rules #.split(", ")
    checkList = ["shiny gold"]
    while len(checkList) != 0:
        focusBag = checkList[0]
        delList = []
        for bagType in dict:
            if focusBag in dict[bagType]:
                checkList.append(bagType)
                total += 1
                delList.append(bagType)
        for bT in delList:
            del dict[bT]
        checkList.remove(focusBag)
    return total

def main():
    print("Golden Bag Sum: " + str(day7p1()))

if __name__ == "__main__":
    main()