'''
Binary to Decimal

Instructions
->Problem Description:
You are given a string binary_str representing a binary number. Your task is to convert this binary string to its corresponding decimal integer. Do not use any built-in functions for conversion.

Input:
A string binary_str, consisting of characters '0' and '1', where the length of the string is between 1 and 30 (inclusive).
->Output:
An integer representing the decimal value of the binary string

Example:
->Input: binary_str = "101"
Output: 5
->Input: binary_str = "1101"
Output: 13
'''

print("Program: Binary to Decimal Converter")
print()
print("Note: Input only binary string, consisting of characters '0' and '1', where the length of the string is between 1 and 30 (inclusive)") 
print()

def binToDec(n):
    z = n[::-1]
    k = 0
    for m in range(len(z)):
        k += int(z[m]) * (2**int(m))
    return k


progRun = True

while progRun:
    try:
        inBin = True   
        while inBin:
            inNum = input("Enter a binary string, n: ")
            inValidIn = False
            for i in inNum:
                if i not in ["0","1"]:
                    inValidIn = True                   
            if len(inNum) > 30 or len(inNum) <1 or inValidIn:
                print("Invalid Input!!")
                inBin = True
            else:
                inBin = False
                
        print("Decimal version: ", binToDec(inNum))
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