# Hemit Patel
# 781159
# ICS3U0-4 
# MR VEERA 
# VOTE COUNT 
# 14 oct 2024

amount_votes = int(input(""))
vote_seq = input("")

a_count = 0
b_count = 0

# The vote seq contains the votes for either A or B
# Go through each character to figure out if it is A or B
# And increment the respective counter

for vote in vote_seq:
    if (vote == "A"):
        a_count += 1
    # Could also use else but what if the character was not B?
    # It would still increment the b count because it is any 
    # scenario other than i == A

    elif (vote == "B"):
        b_count +=1


# Now see the results

if (a_count == b_count):
    print("Tie")

elif (a_count > b_count):
    print("A")

# A count is less than b count meaning b count is higher
# Did it this way instead of b_count > a_count to be consistent
# With my elif statements for better readability

elif (a_count < b_count):
    print("B")
