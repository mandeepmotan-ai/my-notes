'''
Hollow Right Triangle

Instructions
->Problem Description:
You are given an integer n. Your task is to return a hollow right-angled triangle pattern of '*', where the first and last rows contain stars, while the inner rows contain a star at the beginning and end, with spaces in between. The triangle should be right-aligned.

Input:
A single integer n, where 1 <= n <= 100.
Output:
Print Pattern representing rows of stars in the hollow right-angled triangle.

Example:
Input: 4
Output:
     *
   **
  * *
****
'''

num13 = int(input("Enter an integer to specify the size of a hollow right triangle pattern you want to print: "))
print()

#num13 = 20

def hollowRightTriangle(n):
    for i in range(1,n+1):
        if i == 1:
            print(" "*(n-i)+"*")
        elif i == n:
            print("*"*n)
        else:
            print(" "*(n-i)+"*"+" "*(i-2)+"*")
        
hollowRightTriangle(num13)