# Hemit Patel
# 781159
# ICS3U0-1
# Flipper
# MR VEERA
# 15 jan 2025

instructions = input()
grid = ["1", "2", "3", "4"]

def flip_horizonal(grid):
    new_grid = [grid[2], grid[3], grid[0], grid[1]]

    return new_grid

def flip_vertical(grid):
    new_grid = [grid[1], grid[0], grid[3], grid[2]]
    return new_grid

for instruction in instructions:
    if (instruction == "H"):
        grid = flip_horizonal(top, bottom)
    
    elif (instruction == "V"):
        grid = flip_vertical(top, bottom)

print(" ".join([grid[0], grid[1]]))
print(" ".join([grid[2], grid[3]))
