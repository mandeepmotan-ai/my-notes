'''
Right Angled Triangle with Numbers

Instructions
->Problem Description:
You are given an integer n. Your task is to return a right-angled triangle pattern where each row contains repeated digits. The first row contains the number 1 repeated once, the second row contains the number 2 repeated twice, and so on until the nth row contains the number n repeated n times.

Input:
A single integer n, where 1 <= n <= 100.
Output:
Print a pattern where "*" filled in w row in the triangle. The ith row contains the digit i repeated i times.

Example:
Input: 5
Output:
    1
    22
    333
    4444
    55555
'''

num8 = int(input("Enter an integer to specify the size of a right-angled traingle pattern with numbers you want to print: "))
print()

def rightTriangleNumbers(n):
    for i in range(n):
        print(str(i)*i)

rightTriangleNumbers(num8)