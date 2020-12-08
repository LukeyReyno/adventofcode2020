def day2p1():
    total = 0
    inFile = open("files/day2p1.txt", 'r')
    for line in inFile:
        tempStr = line.split()
        lowerLimit = int(tempStr[0].split("-")[0])
        upperLimit = int(tempStr[0].split("-")[1])
        instanceChar = tempStr[1][0]
        password = tempStr[2]
        charCount = 0
        for char in password:
            if char == instanceChar:
                charCount += 1
        if lowerLimit <= charCount <= upperLimit:
            total += 1
    return total

def main():
   print(day2p1())

if __name__ == "__main__":
    main()