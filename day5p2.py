def day5p2():
    inFile = open("files/day5.txt", 'r')
    dict = {} #dict full of row sequences and frequencies
    rowBLen = 7
    colBLen = 3
    for line in inFile:
        rowStr = line[:rowBLen]
        colStr = line[rowBLen:-1]
        try:
            dict[rowStr][0] += 1
            dict[rowStr] += [colStr]
        except:
            dict[rowStr] = [1, colStr]
    
    lst = [] #info of row with 7 occurences
    for r in dict:
        if dict[r][0] == 2**colBLen - 1:
            lst += [r] 
            lst += [dict[r][1:]]
    
    colSum = 0
    for c in lst[1]:
        colSum += int(toBinary(c), base=2)
    col = (2**colBLen - 1) * (2**(colBLen-1)) - colSum 
    #the Summation of all possible row values minus the found values returns the col vaule
    # 7 * 4 = 28 - 21 = 7 <-- column value

    row = int(toBinary(lst[0]), base=2)
    seatID = (row*8) + col
    return seatID

def toBinary(str): #assuming string with F and B chars or L and R chars
    bin = ""
    for char in str:
        if char == 'F' or char =='L':
            bin += '0'
        elif char == 'B' or char == 'R':
            bin += '1'
    return bin

def main():
    print("SeatID: " + str(day5p2()))

if __name__ == "__main__":
    main()