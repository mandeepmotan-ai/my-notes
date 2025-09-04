'''
Area of a Rectangle

Instructions
->Problem Description:
You are given the length and breadth of a rectangle. Your task is to compute and return the area of the rectangle.

Formula:
To calculate the area of a rectangle:
Area=length×breadth

Input:
Two floating-point numbers, length and breadth, representing the dimensions of the rectangle.
Output:
A floating-point number representing the area of the rectangle.

Example:
->Input: length = 5, breadth = 3
Output: 15.0
->Input: length = 7.5, breadth = 2.4
Output: 18.0
'''

print("Program: Area of rectangle calculator")
print()

def areaRectangle(a,b):
    return a*b

progRun = True

while progRun:
    try:
        length = float(input("Enter length value: "))
        breadth = float(input("Enter breadth value: "))
        print("Area of rectangle = ",areaRectangle(length,breadth))
        print()
        contExit = input("Enter y to contine or n to exit!\n")
        while contExit not in ["y","n"]:
            print("Choose from given options!")
            print()
        if contExit == "y":
            continue
        elif contExit == "n":
            progRun = False
        
    except:
        print("Invalid input!!")
        print()
        