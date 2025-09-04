'''
Inverted Pyramid Pattern

Instructions
->Problem Description
You are given an integer n. Your task is to return an inverted pyramid pattern of '*', where each side has n rows, represented as a list of strings. The first row has 2n - 1 stars, the second row has 2n - 3 stars, and so on, until the last row has 1 star, with each row centered using spaces.

->Input Parameters:
n (int): The number of rows in the inverted pyramid.
->Output
Print a pattern where each "*" are used to print each row of the inverted pyramid.

Example:
->Input: 3
->Output:
    
    *****
      *** 
        * 
'''

num7 = int(input("Enter an integer to specify the size of an inverted pyramid pattern you want to print: "))

#num7=10

print()

def invertedPyramid(n):
    for i in range(n,0,-1):
        print(" "*(n-i) +"*"*(2*i-1))


invertedPyramid(num7)