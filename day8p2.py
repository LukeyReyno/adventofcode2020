def day8p2():
    inFile = open("files/day8.txt", 'r')
    instructions = []
    for line in inFile:
        instructions += [line]
    finalI = len(instructions)-1
    indexes = {}
    index = 0
    acc = 0
    check = 0 #variable deciding which nop or jmp to skip
    checked = 0
    cont = True
    while cont:
        value = instructions[index]
        command = value[:3] #line command
        try: #checks if command has been traversed
            indexes[index]
            checked += 1
            check = checked
            indexes = {} #reset loop with larger check value
            index = 0
            acc = 0
            continue
        except:
            indexes[index] = 0
        if check == 0:
            if command == "nop":
                command = "jmp"
            elif command == "jmp":
                command = "nop"
        if index == finalI:
            cont = False
        if command == "nop":
            index += 1
            check -= 1
        elif command == "acc":
            index += 1
            acc += int(value[4:])
        elif command == "jmp":
            index += int(value[4:])
            check -= 1
    return acc
        
        


def main():
    print("Accumulator Value: " + str(day8p2()))

if __name__ == "__main__":
    main()