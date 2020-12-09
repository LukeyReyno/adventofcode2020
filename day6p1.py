def day6p1():
    total = 0 #valid groups
    inFile = open("files/day6.txt", 'r')
    groups = []
    str = ""
    for line in inFile:
        str += line
    str = str.split("\n\n")
    for information in str:
        groups += [information.replace('\n', '')]
    
    for questionStr in groups:
        dict = {}
        for question in questionStr:
            try:
                dict[question] += 1
            except: #adds one to the total if it doesn't exist in dict
                dict[question] = 1
                total += 1
    return total

def main():
    print("Sum Count: " + str(day6p1()))

if __name__ == "__main__":
    main()