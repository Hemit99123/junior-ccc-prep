amount = int(input()

uppercase_letters = ""
current_number = ""
total = 0

for _ in range(amount):
  product_code = input()

  for idx in range(len(product_code)):
      char = product_code[idx]
  
      if char.isupper():
          uppercase_letters += char
      elif char == "-":
          current_number += "-"
      elif char.isdigit():
          current_number += char
          # Check if next character ends the number sequence
          if idx == len(product_code) - 1 or not product_code[idx + 1].isdigit():
              total += int(current_number)
              current_number = ""
  
  final_product_code = uppercase_letters + str(total)
  print(final_product_code)
