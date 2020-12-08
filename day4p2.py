def day4p2():
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
            data = term[4:]
            if field == "byr":
                try:
                    if 1920 <= int(data) <= 2002:
                        dict["byr"] = True
                except: #excepts mark invalid results
                    continue
            elif field == "iyr":
                try:
                    if 2010 <= int(data) <= 2020:
                        dict["iyr"] = True
                except:
                    continue
            elif field == "eyr":
                try:
                    if 2020 <= int(data) <= 2030:
                        dict["eyr"] = True
                except:
                    continue
            elif field == "hgt":
                try:
                    unit = data[-2:]
                    if unit == "cm":
                        if 150 <= int(data[:-2]) <= 193:
                            dict["hgt"] = True
                    elif unit == "in":
                        if 59 <= int(data[:-2]) <= 76:
                            dict["hgt"] = True
                except:
                    continue
            elif field == "hcl":
                valid = True
                if data[0] == '#' and len(data) == 7:
                    for char in data[1:]:
                        if (not (ord('a') <= ord(char) <= ord('f') or ord('0') <= ord(char) <= ord('9')) ):
                            valid = False
                    if valid:
                        dict["hcl"] = True
            elif field == "ecl":
                if data in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    dict["ecl"] = True
            elif field == "pid":
                try:
                    int(data)
                    if len(data) == 9:
                        dict["pid"] = True
                except:
                    continue
        if (dict["byr"] == dict["iyr"] == dict["eyr"] == dict["hgt"] == dict["hcl"] ==
            dict["ecl"] == dict["pid"] == True):
            total += 1
    return total

def main():
    print("Valid Passports: " + str(day4p2()))

if __name__ == "__main__":
    main()