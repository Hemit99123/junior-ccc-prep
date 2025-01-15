# Hemit Patel
# 781159
# ICS3U0-1
# Flipper
# MR VEERA
# 15 jan 2025

instructions = input()
top = [1,2]
bottom = [3,4]
for (instruction in instructions):
    if (instruction == "H"):
        new_bottom = [top[0], top[1]]
        new_top = [bottom[0], bottom[1]]

        top = new_top
        bottom = new_bottom
    
    elif (instruction == "V"):
        new_bottom = [bottom[1], bottom[0]]
        new_top = [top[1], top[0]]

        top = new_top
        bottom = new_bottom

print(top)
print(bottom)