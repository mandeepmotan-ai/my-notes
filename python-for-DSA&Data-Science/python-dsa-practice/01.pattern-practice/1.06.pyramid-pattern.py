'''
Pyramid Pattern

Instructions
Problem Description:
You are given an integer n. Your task is to return a pyramid pattern of '*' where each side has n rows, represented as a list of strings. The pyramid is centered, with 1 star in the first row, 3 stars in the second row, and so on, increasing by 2 stars per row until the base row has 2n - 1 stars.

Input: A single integer n, where 1 <= n <= 100.
Output:
Print a pyramid pattern where each row contains stars ('*') centered, forming a pyramid shape. Each row has an increasing number of stars, with appropriate spaces for centering.

Example:
Input: 3
Output:
           *  
         *** 
       *****
'''

num6 = int(input("Enter an integer to specify the size of a pyramid pattern you want to print: "))
print()

def printPyramid(n):
    for i in range(1,n+1):
        print(" "*(n-i)+"*"*i+"*"*(i-1))

printPyramid(num6)