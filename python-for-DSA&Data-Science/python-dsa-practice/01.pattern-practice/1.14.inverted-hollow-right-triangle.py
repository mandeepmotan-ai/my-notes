'''
Hollow Inverted Right Triangle

Instructions
->Problem Description:
You are given an integer n. Your task is to return a hollow inverted right-angled triangle pattern of '*', where the first row contains n stars, while the inner rows contain a star at the beginning and end, with spaces in between. The triangle should be left-aligned.

Input:
A single integer n, where 1 <= n <= 100.
Output:
Pattern printed where * represents row in the hollow inverted right-angled triangle.

Example:
Input: 5
Output:
    *****
      *   *
        * *
         **
           *
'''

num14 = int(input("Enter an integer to specify the size of a inverted hollow right angled triangle pattern you want to print: "))
print()

#num14 = 50

def invertedHollowRightTriangle(n):
    for i in range(n,0,-1):
        if i == n:
            print(" "*(n-i) +"*"*n)
        elif i == 1:
            print(" "*(n-i) + "*")
        else:
            print(" "*(n-i)+"*"+" "*(i-2)+"*")
 
invertedHollowRightTriangle(num14)
