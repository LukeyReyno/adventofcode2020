from day9p1 import *

def day9p2():
    inFile = open("files/day9.txt", 'r')
    invalidNum = day9p1()
    nums = [int(inFile.readline())]
    s = sum(nums)
    while s != invalidNum:
        if s > invalidNum:
            nums = nums[1:]
        else:
            l = int(inFile.readline())
            nums.append(l)
        s = sum(nums)
    nums.sort()
    return nums[0] + nums[-1]    
            
def main():
    print("Encryption Weakness: " + str(day9p2()))

if __name__ == "__main__":
    main()
