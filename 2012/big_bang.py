# Hemit Patel
# 781159
# MR VEERA
# ICS3U0-4
# 17 jan 2025
# ccc 12 j4

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

k = int(input())
encoded = input()
decoded = ""

for p in range(len(encoded)):

    # p will start at value 0, however our formula (3p*k) 
    # needs p to start at value 1
    position = p + 1 
    letter = encoded[p]

    # we are finding the position of letter relative to the alphabet 
    #(this way we can shift from that pos)

    current_pos = alphabet.index(letter)

    # now based on the current position, shift backwards since we are decoding 
    # there are times where this will yield negative values but python is equipped to handle with that
    original_pos = (current_pos - (3*position + k))
    decoded += alphabet[original_pos]

print(decoded)