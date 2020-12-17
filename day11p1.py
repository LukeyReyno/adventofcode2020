import copy

def day11p1():
    inFile = open("files/day11.txt", 'r')
    grid = []
    line = inFile.readline()
    while line != "":
        grid += [list(line[:-1])] #gets rid of \n
        line = inFile.readline()
    
    while grid != changeGrid(grid):
        grid = changeGrid(grid)
    return occupiedCounter(grid)

def changeGrid(grid):
    newGrid = copy.deepcopy(grid)
    r = 0
    for row in grid:
        c = 0
        for seat in row:
            if seat == ".":
                c += 1
                continue
            elif seat == "L":
                if emptyCheck(r, c, grid):
                    newGrid[r][c] = "#"
                c += 1
                continue
            elif seat == "#":
                if occupiedCheck(r, c, grid):
                    newGrid[r][c] = "L"
                c += 1
                continue
        r += 1
    return newGrid

def emptyCheck(row, col, grid):
    adjacentSeats = [seat(row+1, col), seat(row+1, col+1), seat(row, col+1), seat(row-1, col+1), 
        seat(row-1, col), seat(row, col-1), seat(row+1, col-1), seat(row-1, col-1)]
    for s in adjacentSeats:
        if s.row < 0 or s.row > len(grid)-1 or s.col < 0 or s.col > len(grid[row])-1:
            continue
        elif grid[s.row][s.col] == "#":
            return False
    return True

def occupiedCheck(row, col, grid):
    occupiedTotal = 0
    adjacentSeats = [seat(row+1, col), seat(row+1, col+1), seat(row, col+1), seat(row-1, col+1), 
        seat(row-1, col), seat(row, col-1), seat(row+1, col-1), seat(row-1, col-1)]
    for s in adjacentSeats:
        if s.row < 0 or s.row > len(grid)-1 or s.col < 0 or s.col > len(grid[row])-1:
            continue
        if grid[s.row][s.col] == "#":
            occupiedTotal += 1
    if occupiedTotal >= 4:
        return True
    return False

def occupiedCounter(grid):
    occupiedTotal = 0
    for row in grid:
        for seat in row:
            if seat == "#":
                occupiedTotal += 1
    return occupiedTotal

class seat():
    def __init__(self, row, col):
        self.row = row
        self.col = col

def main():
    print("Occupied Seats: " + str(day11p1()))

if __name__ == "__main__":
    main()
