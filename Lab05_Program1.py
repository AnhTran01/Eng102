# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Anh Tran, Christian Kirk, Inesh Raju, Benjamin Wu
# Section:     410
# Assignment:  LAB 01
# Date:        17 / 09 / 2019

# initialize variables
banana_peel = 0
time = 0
init_vel = 0
fin_vel = 88
dist = 0
user_dist = float(input("Enter distance: "))
counter = 0
TOL = 10**-2
count = 0

#iteration
while time <= 10 and dist < user_dist:
    dist = 0.5 * fin_vel * time + init_vel * time
    time += 0.00005

    # as calculated distance approach the user distance, the time increment decrease for a more accurate result
    if abs(dist - user_dist) < 0.1:
        time += 0.0000005
    elif abs(dist - user_dist) < 10**-4:
        time += 0.00000005
    elif abs(dist - user_dist) < 10**-6:
        time += 0.0000000005
    elif abs(dist - user_dist) < 10**-8:
        time += 0.0000000000005

    #add 1 banana peel every 120 iteration
    counter += 1
    if (counter % 120 == 0):
        banana_peel += 1

# output
if(dist < user_dist):
    print("Marty will make it at t = " + str(time) + " second")
else:
    print("Marty will not make it, fusion update started")
print(str(banana_peel) + " banana peels were used to calculate the time")