def get_cyclic_shifts(string):
    """Generate all possible cyclic shifts of a string."""
    shifts = []
    length_str = len(string)
    for i in range(length_str):
        # Move i characters from start to end
        shift = string[i:] + string[:i]
        shifts.append(shift)
    return shifts

string = input()
user_text = input()

shifts = get_cyclic_shifts(string)

def check_cyclic_shifts(shifts, user_text):
  for shift in shifts:
      if shift in user_text:
            return "yes"
      return "no"

print(check_cyclic_shifts(shifts, user_text))
