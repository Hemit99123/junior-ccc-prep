# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# AmeriCanadian
# 28 oct 2024

vowels = ["a", "e", "i", "o", "u", "y"]

# since the program needs a command to terminate, it would run forever until the program ends by user
# to do this we use an infinte loop

while True:
  user_input = input()

  if (user_input == "quit!"):
    break;
  
  # tokenizing the input so that we can look at each letter one by one 
  # tokenization means breaking each letter of a string into something known as a token (character/letter)
  
  word = list(user_input)
  
  output = ""
  
  # checking if the word is american
  # we first look at the length of the word list which must be 4 tokens long
  # then we check the reverse idx for the list so we can check the last values in which the last 3 have certian cretia to follow 
  # for -2 (second last) index it must be o and the last index (-1) must be r 
  # the thrid last value must be a constant which means it is the opposiste of a vowel so it should not be part of the vowel permitted list 
  
  if (len(word) >= 4 and word[-2] == "o" and word[-1] == "r" and word[-3] not in vowels):
    # we convert by taking the list from 0 to the second last value (non inclusive)
    # this way we can replace the suffix which is the second last and last value or
    # to the new suffix which in an another list of ["o", "u", "r"]
    # this will add both of them up, connecting them to one another 
    
    new_word = word[:-2] + ["o", "u", "r"]
    output = "".join(new_word)

  # if this conditions were not meet, it means the word is not american spelling so no need to convert it
  else:
    output = "".join(word)

  print(output)