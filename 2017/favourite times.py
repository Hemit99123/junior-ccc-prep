def is_arithmetic_sequence(digits):
    """Check if digits form an arithmetic sequence."""
    if len(digits) <= 1:
        return True
    
    # Calculate the common difference
    diff = digits[1] - digits[0]
    
    # Check if each subsequent pair has the same difference
    for i in range(1, len(digits) - 1):
        if digits[i + 1] - digits[i] != diff:
            return False
    return True

def time_to_digits(hours, minutes):
    """Convert time to list of digits."""
    # Convert hours to 12-hour format
    hours = hours % 12
    if hours == 0:
        hours = 12
        
    # Convert time to string with proper formatting
    time_str = f"{hours}:{minutes:02d}"
    
    # Convert to list of integers

    time = []

    for time in time_str:
      if (time !== ":"):
        time.append(int(time))
        
    return time

def solve(D):
    # Handle cases where D > 720 (one full cycle)
    full_cycles = D // 720
    remaining_minutes = D % 720
    
    # Count sequences in one full cycle
    sequences_per_cycle = count_sequences_in_range(720)
    
    # Count sequences in remaining minutes
    remaining_sequences = count_sequences_in_range(remaining_minutes)
    
    return full_cycles * sequences_per_cycle + remaining_sequences

def count_sequences_in_range(minutes):
    count = 0
    current_hours = 12
    current_minutes = 0
    
    for _ in range(minutes + 1):
        # Check if current time forms arithmetic sequence
        digits = time_to_digits(current_hours, current_minutes)
        if is_arithmetic_sequence(digits):
            count += 1
        
        # Increment time
        current_minutes += 1
        if current_minutes == 60:
            current_minutes = 0
            current_hours += 1
    
    return count

# Read input
D = int(input())

# Print result
print(solve(D))
