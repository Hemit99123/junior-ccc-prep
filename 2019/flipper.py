# Hemit Patel
# 781159
# ICS3U0-1
# Flipper
# MR VEERA
# 15 jan 2025

instructions = input()

top = ["1","2"]
bottom = ["3","4"]

def flip_horizonal(top, bottom):
    new_bottom = top
    new_top = bottom

    return new_bottom, new_top

def flip_vertical(top, bottom):
    new_bottom = [bottom[1], bottom[0]]
    new_top = [top[1], top[0]]

    return new_bottom, new_top

for instruction in instructions:
    if (instruction == "H"):
        result = flip_horizonal(top, bottom)
        bottom = result[0]
        top = result[1]
    
    elif (instruction == "V"):
        result = flip_vertical(top, bottom)
        bottom = result[0]
        top = result[1]

print(" ".join(top))
print(" ".join(bottom))
