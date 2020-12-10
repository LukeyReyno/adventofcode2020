def day9p1():
    inFile = open("files/day9.txt", 'r')
    l = int(inFile.readline())
    nums = []
    preamble = 25
    while  l != None:
        nums.append(l)
        l = int(inFile.readline())
        if len(nums) == preamble:
            valid = False 
            i = 0
            while i < preamble:
                j = 1
                while j < preamble:
                    if nums[i] + nums[j] == l:
                        valid = True
                        break
                        break
                    j += 1
                i += 1
            if valid == False:
                return l
            nums = nums[1:]
            
def main():
    print("First Illegal Value: " + str(day9p1()))

if __name__ == "__main__":
    main()