def day10p1():
    inFile = open("files/day10.txt", 'r')
    joltages = []
    diff1 = 1 #initial outlet difference
    diff3 = 1 #final adapter difference
    for line in inFile:
        joltages += [int(line)]
    joltages.sort()
    length = len(joltages)
    i = 0
    while i < length-1:
        if joltages[i+1] - joltages[i] == 3:
            diff3 += 1
        else:
            diff1 += 1
        i += 1
    return diff1 * diff3
            
def main():
    print("Total: " + str(day10p1()))

if __name__ == "__main__":
    main()
