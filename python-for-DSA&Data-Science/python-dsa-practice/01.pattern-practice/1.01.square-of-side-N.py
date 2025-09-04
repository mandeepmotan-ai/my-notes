'''
Square of side 'N'

Instructions
Problem Description: You are given an integer n. Your task is to return a square pattern of size n x n made up of the character '*', represented as a list of strings.

Input Parameters:
n (int): The size of the square (number of rows and columns).

Output:
Print a pattern where each string is a row of n *'s.

Example:

Input: 3
Output: 
***
***
***
'''

num1 = int(input("Enter an integer to specify the size of a square pattern you want to print: "))
print()

def printSquare(n):
    for i in range(1,n):
        print("*"*n)

printSquare(num1)
