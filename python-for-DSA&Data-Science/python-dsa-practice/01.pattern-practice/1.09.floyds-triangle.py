'''
Floyds Triangle

Instructions
Problem Description:
You are given an integer n. Your task is to return the first n rows of Floyd’s Triangle, represented as a list of strings. Floyd's Triangle is a triangular array of natural numbers where the first row contains 1, the second row contains 2 and 3, the third row contains 4, 5, and 6, and so on.

Input:
A single integer n, where 1 <= n <= 100.
Output:
Print a pattern of numbers as rows in Floyd's Triangle.

Example:
Input: 4
Output:
    1
    2 3
    4 5 6
    7 8 9 10
'''

num9 = int(input("Enter an integer to specify the size of a floyds triangle pattern you want to print: "))
print()

#num9=10


def floydsTriangle(n):
    currNum = 1
    for i in range(1,n+1):
        for j in range(i):
            print(currNum,end=" ")
            currNum +=1
        print()
        
floydsTriangle(num9)