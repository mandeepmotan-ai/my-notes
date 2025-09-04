'''
Right Angled Triangle

Instructions
Problem Description:
You are given an integer n. Your task is to return a right-angled triangle pattern of '*' where each side has n characters, represented as a list of strings. The triangle has '*' characters, starting with 1 star in the first row, 2 stars in the second row, and so on until the last row has n stars.

Input Parameters:
n (int): The height and base of the right-angled triangle.

Output:
Print a pattern of '*' characters that increases in length from 1 to n row wise.

Example:
Input: 3
Output:
    *
    **
    ***
'''
num4 = int(input("Enter an integer to specify the size of a right angled triangle pattern you want to print: "))
print()

def rightAngledTriangle(n):
    for i in range(1,n+1):
        print("*"*i)

rightAngledTriangle(num4)
    