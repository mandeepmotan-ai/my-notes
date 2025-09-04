'''
Distance covered by a Vehicle

Instructions
->Problem Description:
You are given the speed of a vehicle and the time it has traveled. Your task is to compute and return the distance traveled by the vehicle.

Formula:
To calculate the distance traveled by a vehicle:
Distance=Speed×Time

Input:
Two floating-point numbers, speed and time, representing the speed of the vehicle and the time it has been traveling.
Output:
A floating-point number representing the distance traveled.

Example:
->Input: speed = 60, time = 2
Output: 120.0
->Input: speed = 50.5, time = 1.5
Output: 75.75
'''

print("Program: Distance covered by vehicle calculator")
print()

def distCalc(s,t):
    return s*t

progRun = True

while progRun:
    try:
        speed = float(input("Enter Speed value: "))
        time = float(input("Enter Time value: "))
        print("Vehicles covered Distance = ",distCalc(speed,time))
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