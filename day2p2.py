def day2p2():
    total = 0
    inFile = open("files/day2p1.txt", 'r')
    for line in inFile:
        tempStr = line.split()
        lowerLimit = int(tempStr[0].split("-")[0])
        upperLimit = int(tempStr[0].split("-")[1])
        instanceChar = tempStr[1][0]
        password = tempStr[2]
        if ((password[lowerLimit-1] == instanceChar and password[upperLimit-1] != instanceChar) or \
            (password[lowerLimit-1] != instanceChar and password[upperLimit-1] == instanceChar)):
            total +=1
    return total

def main():
   print(day2p2())

if __name__ == "__main__":
    main()