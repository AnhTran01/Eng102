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
smoker = input("Do you smoke, Y for Yes, N for No")
HDL = int(input("Enter your total HDL: "))
sysBP = int(input("Enter your total Systolic BP: "))
point = 0
risk = 0

#test case
#Female; Age: 37; Age-based score: -3
if (age == 37):
    point += -3
    if(totCol == 250):
        point += 11
elif(age == 71):
    point += 14
    if(totCol == 170):
        point += 1
elif