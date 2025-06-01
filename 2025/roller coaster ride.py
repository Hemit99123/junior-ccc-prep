place_in_line = int(input(""))
number_of_cars = int(input(""))
people_in_car = int(input(""))

total_people_ride = number_of_cars * people_in_car

if (total_people_ride <= place_in_line):
  print("yes")
else:
  print("no")
