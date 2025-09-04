'''
Hollow Square of side 'N'

Instructions
Problem Description:
You are given an integer n. Your task is to return a hollow square pattern of size n x n made up of the character '*', represented as a list of strings. The hollow square has '*' on the border, and spaces ' ' in the middle (except for side lengths of 1 and 2).

Input Parameters:
n (int): The size of the square (number of rows and columns).

Output:
Print pattern where each string is a row of n characters (*), representing a hollow square.

Example:
Input: 4
Output:
    ****
    *   *
    ****
'''

num2 = int(input("Enter an integer to specify the size of a hollow square pattern you want to print: "))

print()

def hollowSquare(n):
    print("*"*n)
    for i in range(1,n-1):
        print("*"+" "*(n-2)+"*")
    print("*"*n)

hollowSquare(num2)
