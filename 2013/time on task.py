# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# Time on Task 
# 15 Jan 2025

total_time = int(input())
num_chores = int(input())
chores = []

# Adding all the chores due by user

for _ in range(num_chores):
    time = int(input())
    chores.append(time)

# Sort chores in ascending order to maximize the number we can complete

chores.sort()

# Count how many chores we can complete

# These are our counter variables that shall be used
chores_completed = 0
time_used = 0

# Add chores one by one until we can't add any more
for chore_time in chores:
    if (time_used + chore_time <= total_time):
        time_used += chore_time
        chores_completed += 1
    else:
        # breaking prematuraly because if it is above total time expected
        # there is no need for futher computation, we have found the amount of chores we can allocate
        break

print(chores_completed)
