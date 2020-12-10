def day8p1():
    inFile = open("files/day8.txt", 'r')
    instructions = []
    for line in inFile:
        instructions += [line]
    indexes = {}
    index = 0
    acc = 0
    cont = True
    while cont:
        value = instructions[index]
        command = value[:3] #line command
        try: #checks if command has been traversed
            indexes[index]
            return acc
        except:
            indexes[index] = 0
        if command == "nop":
            index += 1
            continue
        elif command == "acc":
            index += 1
            acc += int(value[4:])
            continue
        elif command == "jmp":
            index += int(value[4:])
            continue
    

def main():
    print("Accumulator Value: " + str(day8p1()))

if __name__ == "__main__":
    main()