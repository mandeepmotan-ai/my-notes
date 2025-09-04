'''
Number of Rounds of Lift

Instructions
->Problem Description:
You are given n, the total number of people, and capacity, the maximum number of people the lift can carry at a time. All people want to go from the ground floor to the top floor. Your task is to calculate the number of rounds the lift has to make to transport all the people to the top floor.

Input:
Two integers, n and capacity, where n is the total number of people, and capacity is the maximum number of people the lift can carry in one round.
Output:
An integer representing the number of rounds the lift needs to cover to transport all people to the top floor.

Example:
->Input: n = 10, capacity = 3
Output: 4
->Input: n = 7, capacity = 4
Output: 2
'''

print("Program: Number of Rounds of Lift calculator")
print()

def roundCalc(n,c):
    return (n//c)+1

programRun = True

while programRun:
   try:
       numPeop = int(input("Enter Number of people, n: "))
       capaLift = int(input("Enter Capacity of lift, c: "))
       print(f"Number of rounds of lift to carry {numPeop} people in a lift with capacity of {capaLift} people per round is: ",roundCalc(numPeop,capaLift))
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