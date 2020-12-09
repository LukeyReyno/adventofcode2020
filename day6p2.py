def day6p2():
    total = 0 #valid groups
    inFile = open("files/day6.txt", 'r')
    groups = []
    str = ""
    for line in inFile:
        str += line
    str = str.split("\n\n")
    for information in str:
        groups += [information.split()]
    
    for g in groups:
        p1 = g[0]
        for char in p1:
            valid = True
            for p in g[1:]: #makes sure the characters for one person appears in all people
                if (not char in p):
                    valid = False
                    break
            if valid:
                total += 1

    return total

def main():
    print("Sum Count: " + str(day6p2()))

if __name__ == "__main__":
    main()