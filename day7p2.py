def day7p2():
    inFile = open("files/day7.txt", 'r')
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
        dict[name] = rules.split(", ")
    return counter(dict, "shiny gold")

def counter(dict, bagName):
    total = 0
    r = dict[bagName]
    for rule in r:
        try:
            num = int(rule[0]) #number of bags per rule
            newBagName = rule.split()
            newBagName = newBagName[1] + " " + newBagName[2]
            total += num + num*counter(dict, newBagName)
        except: #base case where 'no other bags' are contain
            return 0
    return total

def main():
    print("Golden Bag Sum: " + str(day7p2()))

if __name__ == "__main__":
    main()