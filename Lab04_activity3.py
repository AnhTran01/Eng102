# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Anh Tran, Christian Kirk, Inesh Raju, Benjamin Wu
# Section:     410
# Assignment:  LAB 01
# Date:        17 / 09 / 2019

#Variable
age = int(input("Enter your age: "))
totCol = int(input("Enter your total cholestoral: "))
smoker = input("Do you smoke, Y for Yes, N for No: ")
HDL = int(input("Enter your total HDL: "))
sysBP = int(input("Enter your total Systolic BP: "))
point = 0
risk = 0

#test case goes here
if (29 <= age <= 34):
    point += -7
    if(totCol < 160):
        point += 0
    elif(160 <= totCol <= 199):
        point += 4
    elif(200<= totCol <=239):
        point += 8
    elif(240<= totCol <=279):
        point += 11
    elif(totCol > 279):
        point += 13
    elif(smoker == 'Y'):
        points += 0
    elif(smoker == 'N'):
        point  += 1
    elif()