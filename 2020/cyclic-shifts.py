
s = input()
t = input()
found = False  # Initialize a flag

# Using set for faster lookup
cyclic_set = set()

# Create cyclic permutations
for idx in range(len(t)):
    # Generate the new cyclic permutation
    new_list = t[idx:] + t[:idx]
    cyclic_set.add(new_list)

# Check if any cyclic permutation is in string 
for cyclic in cyclic_set:
    if cyclic in s:
        found = True
        print('yes')
        break

if not found:
    print('no')
