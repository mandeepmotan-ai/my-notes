'''
Check for Prime Number

Instructions
->Problem Description:
You are given an integer n. Your task is to check whether the number is prime or not. A prime number is a number greater than 1 that has no divisors other than 1 and itself. Return True if the number is prime, and False otherwise.

Input:
A single integer n where 1 <= n <= 10^6.
Output:
Return True if n is a prime number, otherwise return False.

Example:
->Input: n = 5
Output: True
->Input: n = 4
Output: False
'''

print("Program: Prime Number Checker")
print()

def primeChecker(n):
    chk = True
    if n in [1,2,n%2==0]:
        chk = False
    m = 3
    while m*m <= n:
        if n%m == 0:
            chk = False
        m += 2
    return chk

progRun = True

while progRun:
    try:
        inNum = int(input("Enter an integer (1 <= n <= 10^6), n: "))
        print("Number found Prime: ",primeChecker(inNum))
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


    