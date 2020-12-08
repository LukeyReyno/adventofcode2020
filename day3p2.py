def day3p2(dx, dy):
    total = 0
    inFile = open("files/day3p1.txt", 'r')
    row = 0
    col = 0
    puzzle = []
    for line in inFile:
        puzzle.append(line[:-1])
    while row + dy < len(puzzle):
        row += dy
        col = (col + dx) % (len(puzzle[row]))
        if puzzle[row][col] == "#":
            total += 1
    return total

def main():
    print("Tree Count: " + str(day3p2(1, 1)))
    print("Tree Count: " + str(day3p2(3, 1)))
    print("Tree Count: " + str(day3p2(5, 1)))
    print("Tree Count: " + str(day3p2(7, 1)))
    print("Tree Count: " + str(day3p2(1, 2)))
    print("Answer: " + str(day3p2(1, 1)* day3p2(3, 1)* day3p2(5, 1)* day3p2(7, 1)* day3p2(1, 2)))

if __name__ == "__main__":
    main()