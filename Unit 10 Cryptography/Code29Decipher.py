# Ben Koczwara
# Dec.5,2013
# to create a program that will decipher a message using Code 29

print "Code 29 Decipher"
print "----------------"
print
print "This program will create an encrypted message using Code 29"
print
again = "y"
while again == "y":
      numbers = []
      new_numbers = []
      code = ""
      message = raw_input("Enter the code to decipher: ")
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
      print
      for z in message:
            if z.isalpha():
                  num = ord(z)
                  num -= 62
                  numbers.append(num)
            else:
                  numbers.append(int(z))

      for q in range((len(numbers)-1),-1,-1):
            n = 1
            if q == len(numbers)-1:
                  x = key
            else:
                  x = new_numbers[-1]

            while n!=0:
                  if (n*x)%29 == numbers[q]:
                        new_numbers.append(n)
                        n = 0
                  else:
                        n+=1

      new_numbers.reverse()
      for a in new_numbers:
            if a <= 2:
                  code += " "
            else:
                  char = chr(a+62)
                  code+=char

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
                  

      
      
                  
                  
            

      

      
      

            
                  
      
            
