def day1p1():
    inFile = open("files/day1p1.txt", 'r')
    numList = []
    for line in inFile:
        numList.append(line)
    for l1 in numList:
        for l2 in numList:
            if int(l1) + int(l2) == 2020:
                return int(l1) * int(l2)

def main():
   print(day1p1())

if __name__ == "__main__":
    main()