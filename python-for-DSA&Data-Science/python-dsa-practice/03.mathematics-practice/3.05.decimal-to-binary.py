'''
Decimal to Binary

Instructions
->Problem Description:
You are given an integer n. Your task is to return its binary representation as a string. Do not use any built-in functions for conversion.

Input:
A single integer n, where -10^9 <= n <= 10^9.
Output:
A string representing the binary representation of n.

Example:
->Input: n = 5
Output: "101"
->Input: n = -5
Output: "-101"
'''

print("Program: Decimal to Binary Converter")
print()

def decToBinary(n):
    binLt = []
    z = n
    isNeg = False
    if str(n)[0] == "-":
        z = int(-n)
        isNeg = True
    while True:
        binLt.append(z%2)
        z = z//2
        if z ==0:
            break
    res = "".join(str(x) for x in binLt)
    if isNeg:
        return -(int(res))
    return res

progRun = True

while progRun:
    try:
        inNum = int(input("Enter a single integer (-10^9 <= n <= 10^9), n: "))
        print("Binary version: ",decToBinary(inNum))
        print()
        goOn = input("Enter y to continue or n to exit: ")
        while goOn not in ["y","n"]:
            print("Choose valid options!!")
            print()
            goOn = input("Enter y to continue or n to exit:")
        print()
        if goOn == "y":
           continue
        elif goOn == "n":
           progRun = False
           print("Program terminated successfully!!")
    except:
        print("Invalid Input!!")
        print()