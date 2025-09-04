'''
Number Pyramid Pattern

Instructions
->Problem Description:
You are given an integer n. Your task is to return a pyramid pattern of numbers, where each row contains increasing numbers starting from 1 up to the row number, and the pyramid is centered with leading spaces.

Input:
A single integer n, where 1 <= n <= 100.
Output:
Pattern printed where numbers represents a row in the pyramid pattern.

Example:
Input: 4
Output:
       1   
     1 2  
    1 2 3 
  1 2 3 4
'''

num15 = int(input("Enter an integer to specify the size of a number pyramid pattern you want to print: "))
print()

#num15 = 9

def numberPyramid(n):
    for i in range(1,n+1):
        print(" "* (n-i),end="")
        for j in range(1,i):
            print(j,end=" ")
        print()

numberPyramid(num15)
        
        