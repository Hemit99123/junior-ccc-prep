# Hemit Patel
# 781159
# June 3rd 2025

total_donuts = int(input())
total_events = int(input())

for _ in range(total_events):
  operation = input()
  donuts = int(input())

  if (operation == "+"):
    total_donuts += donuts 
  else:
    total_donuts -= donuts

print(total_donuts)
