'''
Right Angled Triangle II

Instructions
->Problem Description:
You are given an integer n. Your task is to return a right-angled triangle pattern of '*', where each row contains stars aligned to the right. The first row has one star, the second row has two stars, and so on, until the nth row has n stars.

Input:
A single integer n, where 1 <= n <= 100.
Output:
A list of strings where each string represents a row in the right-angled triangle, right-aligned.

Example:
Input: 4
Output: 
      *
    **
  ***
****
'''

#num11 = int(input("Enter an integer to specify the size of a right-aligned right triangle pattern you want to print: "))
print()

num11 = 10

def rightAlignedRightTriangle(n):
    for i in range(n):
        print(" "*(n-i) + "*"*(i))
 
rightAlignedRightTriangle(num11)