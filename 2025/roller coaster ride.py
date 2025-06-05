# Hemit Patel
# 781159
# June 3rd 2025

place_in_line = int(input(""))
number_of_cars = int(input(""))
people_in_car = int(input(""))

total_people_ride = number_of_cars * people_in_car

# If the place in line is less than total people in ride, there is space for you to enter the ride
if (place_in_line <= total_people_ride):
  print("yes")
  
# There is only one another circumstance
else:
  print("no")
