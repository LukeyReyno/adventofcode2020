def day3p1():
    total = 0
    inFile = open("files/day3p1.txt", 'r')
    col = 0
    inFile.readline()
    for line in inFile:
        col += 3
        if col >= (len(line)-1): # Minus 1 because the \n character
            col %= (len(line)-1)
        if line[col] == "#":
            total += 1
    return total

def main():
   print("Tree Count: " + str(day3p1()))

if __name__ == "__main__":
    main()