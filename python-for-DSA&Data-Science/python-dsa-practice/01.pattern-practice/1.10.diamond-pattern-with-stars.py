'''
Diamond Pattern

Instructions
Problem Description:
You are given an integer n. Your task is to return a diamond pattern of '*' with n rows for the upper part (the widest row will have 2n - 1 stars), and the lower part is the mirrored version of the upper part. Each row should be centered with appropriate spaces.

Input:
A single integer n, where 1 <= n <= 100.
Output:
A list of strings where each string represents a row in the diamond pattern.

Example:
Input: 5
Output:
        *    
      ***   
    *****  
  ******* 
*********
  *******
    *****
     ***   
       * 
'''

num10 = int(input("Enter an integer to specify the size of a diamond pattern of stars you want to print: "))
print()

#num10 = 5

def starsDiamond(n):
    for i in range(n):
        print(" "*(n-i) + "*"*((2*i)-1))
    for i in range(n,0,-1):
        print(" "*(n-i) + "*"*((2*i)-1))

starsDiamond(num10)