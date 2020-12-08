def day1p2():
    inFile = open("files/day1p1.txt", 'r')
    numList = []
    for line in inFile:
        numList.append(line)
    for l1 in numList:
        for l2 in numList:
            for l3 in numList:
                if int(l1) + int(l2) + int(l3) == 2020:
                    return int(l1) * int(l2) * int(l3)

def main():
   print(day1p2())

if __name__ == "__main__":
    main()