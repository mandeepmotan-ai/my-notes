'''
Line Equation

Instructions
->Problem Description:
You are given the slope m and the y-intercept b of a line, along with a value x. Your task is to calculate and return the value of y using the equation of a line in slope-intercept form:
y=mx+b

Input:
Three floating-point numbers: slope, intercept, and x.
Output:
A floating-point number representing the value of yyy corresponding to the given xxx.

Example:
->Input: slope = 2, intercept = 3, x = 4
Output: 11.0
->Input: slope = 1.5, intercept = -2, x = 2
Output: 1.0
'''

print("Program: Line Equation Calculator")
print()

def lineEquation(m,b,x):
    return (m*x)+b

progRun = True

while progRun:
    try:
        slopeM = float(input("Enter Slope value, m: "))
        yInter = float(input("Enter y-Intercept b value, b: "))
        valX = float(input("Enter value x: "))
        print("Equation of line = ",lineEquation(slopeM,yInter,valX))
        print()
        goOn = input("Enter y to continue or n to exit: ")
        while goOn not in ["y","n"]:
            print("Choose valid options!!")
            print()
            goOn = input("Enter y to continue or n to exit:")
        print()
        if goOn == "y":
           continue
        elif goOn == "n":
           progRun = False
           print("Program terminated successfully!!")
    except:
        print("Invalid Input!!")
        print()