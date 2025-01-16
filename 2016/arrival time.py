# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# Arrival Time 
# jan 15 2025 

# Define rush hour periods in minutes (from 00:00)

MORNING_RUSH_START = 7 * 60  # 07:00
MORNING_RUSH_END = 10 * 60   # 10:00
EVENING_RUSH_START = 15 * 60 # 15:00
EVENING_RUSH_END = 19 * 60   # 19:00

# Get input time and convert to minutes since midnight
time_input = input().split(":")

# Convert to minutes so its easier to handle and compute with
current_time = int(time_input[0]) * 60 + int(time_input[1])

# Normal commute takes 240 minutes (4 hours) in rush hour time
# When not in rush hour, time passes twice as fast (so takes 2 hours)
remaining_progress = 240

# Simulate time passing minute by minute
# With every minute, we update our elpased time

while remaining_progress > 0:
    # Check if current time is during rush hour
    is_rush_hour = (MORNING_RUSH_START < current_time < MORNING_RUSH_END or 
                   EVENING_RUSH_START < current_time < EVENING_RUSH_END)

    if is_rush_hour:
        remaining_progress -= 1  # In rush hour, 1 minute of progress
    else:
        remaining_progress -= 2  # Outside rush hour, 2 minutes of progress
    
    # Rush hour has 1 minute of progress whilst non rush hour has 2 mins because progress is HALF the amount in rush traffic

    # Update to new time, always assume one minute has passed even with 2 mins of progress have been completed
    # This is because the road traffic conditions within non rush hours is better therefore more progress can be made
    
    current_time += 1
    
# Round up times ending in '9' to the next multiple of 10
# This is needed because:
# 1. Our calculations (adding 1s and 2s) can reach times ending in 9
# 2. From a '9' ending, our next step could create an invalid time
# 3. So we push it forward to ensure we stay on valid intervals (00,20,40)

if current_time % 10 == 9:
    current_time += 1
    
# Convert final time back to hours and minutes

# We use the %24 to wrap around midnight (24:00)
# This way, once we reach hour 24 it goes back to 00

hours = (current_time // 60) % 24 
minutes = current_time % 60

# Format output time back to HH:MM format using f strings (same as format function)

arrival_time = f"{hours:02d}:{minutes:02d}"

print(arrival_time)
