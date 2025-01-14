# Hemit Patel
# 781159
# ICS3U0-4
# J1 2023 Solution
# mr veera
# 21 sep 2024

# Number of days (input)
num_days = int(input())

# Dictionary to store the count of "Y" for each day
day_counts = {}

# Output string to store the days with the maximum "Y" count
result = ""

# Loop through the input for each day
for _ in range(num_days):
    attendance = input()  # List of "Y" or "N" indicating attendance for the day

    # Loop through each day's attendance
    for day_index in range(len(attendance)):
        # Calculate the day number (starting from 1)
        day_number = day_index + 1

        # If the attendance is "Y", update the day count
        if attendance[day_index] == "Y":
            if day_number in day_counts:
                day_counts[day_number] += 1  # Increment the count for the day
            else:
                day_counts[day_number] = 1  # Initialize the count for the day

# Find the maximum count of "Y" for any day
max_attendance = max(day_counts.values())

# Loop through the dictionary to find the days with the maximum "Y" count
for day, count in day_counts.items():
    if count == max_attendance:
        result = result + str(day) + ","  # Add the day to the result string

# Remove the trailing comma and return the result
print(result.rstrip(','))
