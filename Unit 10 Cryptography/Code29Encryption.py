# Ben Koczwara
# Dec.5,2013
# to create a program that will encrypt a message using Code 29

import random

print "Code 29 Encryptor"
print "-----------------"
print
print "This program will create an encrypted message using Code 29"
print
again = "y"
while again == "y":
      numbers = []
      code = ""
      go = False
      while not go:
            try:
                  key = int(raw_input("Enter the secret key: "))
                  if 1 <= key <= 28:
                        go = True
                  else:
                        crash
            except:
                  print
                  print "The key must be a whole number greater than 1 and less than 28"
                  print
                  
      message = raw_input("Enter the message you wish to encrypt: ").upper()
      for z in message:
            if z == " ":
                  replace = random.randint(1,2)
                  numbers.append(replace)
            elif z.isalpha():
                  num = ord(z)
                  num -= 62
                  numbers.append(num)

      for w in range(0,len(numbers)):
            if w != (len(numbers)-1):
                  value = numbers[w] * numbers[w+1]
                  numbers[w] = value
            else:
                  value = numbers[w] * key
                  numbers[w] = value

      for w in range(0,len(numbers)):
            new = numbers[w]%29
            numbers[w] = new

      for c in numbers:
            if c > 2:
                  c+=62
                  char = chr(c)
                  code += char
            else:
                  code += str(c)
      print
      print "The coded message is:"
      print code
      print

      run_again = False
      while not run_again:
            again = raw_input("Would you like to run the program again (y/n): ").lower()
            if again != "":
                  run_again = True
            else:
                  print "You must enter something"

      again = again[0]
      print

      
