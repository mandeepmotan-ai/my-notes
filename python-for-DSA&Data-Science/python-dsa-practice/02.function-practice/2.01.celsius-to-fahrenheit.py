'''
Celsius to Fahrenheit

Instructions
->Problem Description:
You are given a temperature in Celsius. Your task is to convert it to Fahrenheit and return the result.

Formula:
To convert Celsius to Fahrenheit, use the formula:
F = (9/5 * C) + 32
Where F is the temperature in Fahrenheit and C is the temperature in Celsius.

Input:
A floating-point number C representing the temperature in Celsius.
Output:
A floating-point number representing the temperature in Fahrenheit.

Example:
->Input: C = 25
Output: 77.0

->Input: C = 0
Output: 32.0
'''

print("Program:  Celsius to Fahrenheit converter")
print()

programRun = True

def celToFah(n):
    return ((9/5)*n) +32

while programRun:
   celsIn = input("Enter Celsius value: ")
   try:
       celsIn = float(celsIn)
       print("Faherenheit value = ",celToFah(celsIn))
       print()
       goOn = input("Enter y to continue or n to exit:")
       while goOn not in ["y","n"]:
            print("Choose valid options!!")
            print()
            goOn = input("Enter y to continue or n to exit:")
            print()
       if goOn == "y":
           continue
       elif goOn == "n":
           programRun = False
           print("Program terminated successfully!!")
   except:
       print("Enter valid input!!")
       print()
   
    
        