# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# Triangle Times
# 14 oct 2024

angle_1 = int(input(""))
angle_2 = int(input(""))
angle_3 = int(input(""))


# Some variables needed for the conditonal statement 
# This will make it easier for devs to read my program
# Also helps reduce reduncny in my program which means
# It is following the DRY principle (do not repeat yourself)

sum_angles = angle_1 + angle_2 + angle_3

# These are the different combinations to see if 2 angles are the same
# There are 6 total but some are un-nesscary as they will produce the same
# operation as one here
# added comparisons into variables to improve readablity

one_two_eq = angle_1 == angle_2
one_three_eq = angle_1 == angle_3
two_three_eq = angle_2 == angle_3

if (sum_angles != 180):
    print("Error")
# Equlateral is checked first for classifying triangles because 60*3 = 180 so it would be true 
# Even if the triangle were Equlateral

elif (angle_1 == 60 and angle_2 == 60 and angle_3 == 60):
    print("Equilateral")
# Same logic here, the Iscosceles is checked first because Scalene would 
# be true even if 2 of the angles are the same as the sum would still be 180
# no need to see if sum is 180 because that was checked in the first if statement 

elif (one_two_eq or one_three_eq or two_three_eq):
    print("Isosceles")

# if none of these combinations hold true than the sum of the angle is still 180 which would be classifed as a scalene

else:
    print("Scalene")
