def day5p1():
    maxSeatID = 0
    inFile = open("files/day5.txt", 'r')
    for line in inFile:
        rowStr = line[:7]
        binaryRow = toBinary(rowStr)
        row = int(binaryRow, base=2)

        colStr = line[7:]
        binaryCol = toBinary(colStr)
        col = int(binaryCol, base=2)

        seatID = (row*8) + col
        if seatID > maxSeatID:
            maxSeatID = seatID
    return maxSeatID

def toBinary(str): #assuming string with F and B chars or L and R chars
    bin = ""
    for char in str:
        if char == 'F' or char =='L':
            bin += '0'
        elif char == 'B' or char == 'R':
            bin += '1'
    return bin

def main():
    print("Highest SeatID: " + str(day5p1()))

if __name__ == "__main__":
    main()