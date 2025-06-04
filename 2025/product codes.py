product_code = input()
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
number = "123456789"

uppercase_letters = ""
integer = 0

for char in product_code:
  if (char in upper) or :
    uppercase_letters += char
  elif (char in number):
    integer += int(char)

final_product_code = uppercase_letters + str(integer)

print(final_product_code)
