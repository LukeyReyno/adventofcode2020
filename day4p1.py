def day4p1():
    total = 0 #valid passports
    inFile = open("files/day4.txt", 'r')
    passports = []
    str = ""
    for line in inFile:
        str += line
    str = str.split("\n\n")
    for information in str:
        passports += [information.split()]
    for passport in passports:
        dict = {
            "byr": False,
            "iyr": False,
            "eyr": False,
            "hgt": False,
            "hcl": False,
            "ecl": False,
            "pid": False,
            "cid": False,
        }
        for term in passport:
            field = term[0:3]
            try:
                dict[field] = True
            except:
                continue
        if (dict["byr"] == dict["iyr"] == dict["eyr"] == dict["hgt"] == dict["hcl"] ==
            dict["ecl"] == dict["pid"] == True):
            total += 1
    return total

def main():
    print("Valid Passports: " + str(day4p1()))

if __name__ == "__main__":
    main()