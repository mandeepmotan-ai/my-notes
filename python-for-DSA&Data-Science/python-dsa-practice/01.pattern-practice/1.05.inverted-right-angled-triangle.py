'''
Inverted Right Angled Triangle

Instructions
Problem Description:
You are given an integer n. Your task is to return an inverted right-angled triangle pattern of '*' where each side has n characters, represented as a list of strings. The first row should have n stars, the second row n-1 stars, and so on, until the last row has 1 star.

Input Parameters:
n (int): The height and base of the inverted right-angled triangle.

Output:
Print a inverted right angled triangle pattern where '*' characters decreases in length from n to 1 row wise

Example:
Input: 3
Output:
    ***
    **
    *
'''

num5 = int(input("Enter an integer to specify the size of an inverted right triangle pattern you want to print: "))
print()

def invertedRightAngle(n):
    for i in range(n,0,-1):
        print("*"*i)

invertedRightAngle(num5)