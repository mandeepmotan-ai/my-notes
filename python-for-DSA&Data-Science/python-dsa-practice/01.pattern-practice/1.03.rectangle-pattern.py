'''
Rectangle Pattern

Instructions
Problem Description:
You are given two integers, n and m. Your task is to return a rectangle pattern of '*', where n represents the number of rows (length) and m represents the number of columns (breadth).

Input:
Two integers n and m, where 1 <= n, m <= 100.

Output:
Print pattern where *'s are used for row of the rectangle pattern.

Example:
Input: n = 4, m = 5
Output:
    *****
    *****
    *****
    *****
'''
print("Enter below dimensions of rectangle pattern to print ->")
n = int(input("Enter length: "))
m = int(input("Enter breadth: "))
print()

def printRectangle(n,m):
    for i in range(1,m+1):
        print("*"*n)
 
printRectangle(n, m)
 
    