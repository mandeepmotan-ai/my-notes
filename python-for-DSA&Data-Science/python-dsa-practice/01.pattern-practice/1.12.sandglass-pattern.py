'''
Sandglass Pattern
->Instructions
Problem Description:
You are given an integer n. Your task is to return a sandglass pattern of '*', where the first row contains 2n - 1 stars and each subsequent row decreases the number of stars by 2, until the last row contains a single star. After reaching the smallest width, the pattern then continues with the same number of stars increasing back to 2n - 1. The stars in each row should be centered.

Input:
A single integer n, where 1 <= n <= 100.
Output:
A list of strings where each string represents a row in the sandglass pattern.

Example:
Input: 4
Output:
    
    *******
      ***** 
        ***  
          *   
        *** 
      ***** 
    *******
'''

num12 = int(input("Enter an integer to specify the size of a Sandglass pattern you want to print: "))
print()

#num12 = 9

def sandglassPattern(n):
    for i in range(n,0,-1):
        print(" "*(n-i) + "*"*((2*i)-1))
    for j in range(2,n+1):
        print(" "*(n-j) + "*"*((2*j)-1))

sandglassPattern(num12)
        