# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# Telemarketer or not? J1 2018

# Each digit is given its own set of input

digit_1 = int(input())
digit_2 = int(input())
digit_3 = int(input())
digit_4 = int(input())

# Added parantheses to each of the conditions so that they generate their own boolean value and then
# using that boolean value in the if statement with the and operator so that ALL conditions must
# be met for this to work

# LEARNED TO PUT THE DIFFERENT CONDITIONS WHEN USING BOOL OPERATORS IN DIFFERENT PARENTHESES WHEN THEY ALL RELY ON EACH OTHER TO BE TRUE 

if (digit_1 == 8 or digit_1 == 9) and (digit_4 == 8 or digit_4 == 9) and (digit_2 == digit_3):
    print("ignore")
else:
    print("answer")

