'''
Check for Even Number

Instructions
->Problem Description:
You are given an integer n. Your task is to check whether the number is even or not. Return True if the number is even, and False otherwise.

Input:
A single integer n where -10^9 <= n <= 10^9.
Output:
Return True if n is an even number, otherwise return False.

Example:
->Input: n = 4
Output: True
->Input: n = 7
Output: False
'''

print("Program: Even Number Checker")
print()

progRun = True

while progRun:
    try:
        inNum = int(input("Enter an integer, n: "))
        inList = [int(inNum)]
        print(f"Number found even: {''.join(['True' if n%2==0 else 'False' for n in inList])}")
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