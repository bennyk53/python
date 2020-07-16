# Name: Ben Koczwara
# Date: Sept.17,2013
# Purpose: to create a program that will crack a coded message that used Caesar ciphers

print "Ceasar Cipher"
print "--------------"
print
print "This program will decode a message that used Ceasar Cipher"
print
again = "y"
while again == "y":
      go = False
      while not go:
            
            code = raw_input("Enter a message to decode: ").upper()
            print

            if code != "":
                  go = True
            else:
                  print "You must enter something"
                  print

      letter = ""
      high = 0
      alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

      for x in alpha:
            occurs = code.count(x)
            
            if occurs > high:
                  high = occurs 
                  letter = x

      num = ord(letter)

      change = num - 69
      
      message = ""
      for x in code:
            if x.isalpha():
                  value = ord(x)
                  value -= change
                  if value < 64:
                        extra = 64 - value
                        value = 90 - extra
                  char = chr(value)
                  message += char
            else:
                  message += x

      print "The decrypted code message is:",message
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

