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
    position = p + 1 
    letter = encoded[p]
    current_pos = alphabet.index(letter)
    original_pos = (current_pos - (3*position + k)) % 26
    decoded += alphabet[original_pos]

print(decoded)