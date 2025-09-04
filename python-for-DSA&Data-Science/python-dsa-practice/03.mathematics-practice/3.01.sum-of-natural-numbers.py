'''
Sum of N Even Natural Numbers

Instructions
->Problem Description:
You are given an integer n. Your task is to calculate and return the sum of the first n even natural numbers. The even natural numbers are: 2, 4, 6, 8, ...

Input:
A single integer n where 1 <= n <= 10^4.
Output:
Return the sum of the first n even natural numbers.

Example:
->Input: n = 3
Output: 12  # (2 + 4 + 6)
->Input: n = 5
Output: 30  # (2 + 4 + 6 + 8 + 10)
'''

print("Program: Sum of N Even natural numbers calculator: ")
print()

def sumCalc(n):
    evenNums = []
    m=1
    while len(evenNums) != n:
                if m%2 == 0:
                    evenNums.append(m)
                m+=1
    return evenNums
                
progRun = True

while progRun:
    try:
        natNum = int(input("Enter an integer, n: "))
        numbers = sumCalc(natNum)
        print(f'Sum of first {natNum} Even Natural numbers is: {sum(sumCalc(natNum))}  # ({" + ".join([str(x) for x in sumCalc(natNum)])})')
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