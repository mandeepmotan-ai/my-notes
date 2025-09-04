'''
Valid Perfect Square

Instructions
->Problem Description:
You are given a positive integer num. Your task is to check whether num is a perfect square or not. A perfect square is an integer that is the square of an integer (e.g., 1, 4, 9, 16, ...). Return True if num is a perfect square, and False otherwise.

Input:
A single positive integer num where 1 <= num <= 10^9.
Output:
Return True if num is a perfect square, otherwise return False.

Example:
->Input: num = 16
Output: True
->Input: num = 14
Output: False
'''

print("Program: Perfect Square Checker")
print()

def squareChk(n):
    chk = False
    m = 1
    while m  <= n//2:
        if m*m == n:
            chk = True
        m+=1
    return chk
        
progRun = True

while progRun:
    try:
        inNum = int(input("Enter an integer (1 <= num <= 10^9), n: "))
        print("Number found Perfect Square: ",squareChk(inNum))
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