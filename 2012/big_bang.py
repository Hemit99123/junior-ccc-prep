# Hemit Patel
# 781159
# MR VEERA
# ICS3U0-4
# 14 jan 2025
# ccc 12 j4


alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

k = int(input())
encoded = input()
decoded = ""

for p in range(len(encoded)):
    letter = encoded[p]
    # Find the current position of the letter in the alphabet
    current_pos = alphabet.index(letter)
    # Calculate the original position by working backwards
    # Add 26 before taking modulo to handle negative numbers correctly
    # p starts at 0 and therefore we must add one to it
    original_pos = (current_pos - (3*(p+1) + k) + 26*100) % 26
    decoded += alphabet[original_pos]

print(decoded)