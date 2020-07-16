# Ben Koczwara
# Dec.12,2013
# create a program that encrypts a Base Three Code

print "Bass Three Code Encryptor"
print "-------------------------"
print
print "This program will encrypt a message using Base Three Code"
print
again = "y"
while again == "y":
      code = ""
      numbers = ""
      new_message = ""
      new_numbers = []
      message = raw_input("Enter the message that you wish to encrypt: ").upper()
      print
      for q in message:
            if q.isalpha():
                  new_message += q
            elif q == " ":
                  new_message += "*"
      for w in new_message:
            
            count = 1
            string = ["0","0","0"]
            change2 = False
            change3 = False
            
            while count <= (ord(w)-65):
                  old_string = string
                  
                  if old_string[2] == "0":
                        string[2] = "1"
                  elif old_string[2] == "1":
                        string[2] = "2"
                  elif old_string[2] == "2":
                        string[2] = "0"
                        change2 = True
                        
                  if change2:
                        if old_string[1] == "0":
                              string[1] = "1"
                        elif old_string[1] == "1":
                              string[1] = "2"
                        elif old_string[1] == "2":
                              string[1] = "0"
                              change3 = True
                  if change3:
                        if old_string[0] == "0":
                            string[0] = "1"
                        elif old_string[0] == "1":
                              string[0] = "2"
                        elif old_string[0] == "2":
                              string[0] = "0"

                  count += 1
                  change2 = False
                  change3 = False
                  
            if w == "*":
                  string  = ["2","2","2"]
            num = ""
            for z in string:
                  num += z

            numbers += num

      list1 = list(numbers[:len(message)])
      list2 = list(numbers[len(message):(2*len(message))])
      list3 = list(numbers[(2*len(message)):])

      for e in range(0,len(message)):
            num = list1[e] + list2[e] + list3[e]
            new_numbers.append(num)

      for nums in new_numbers:
            string = ["0","0","0"]
            count = 0
            if nums == "222":
                  count = -23
                  string = ["2","2","2"]

            while string[0]+string[1]+string[2] != nums:
                  old_string = string
                  if old_string[2] == "0":
                        string[2] = "1"
                  elif old_string[2] == "1":
                        string[2] = "2"
                  elif old_string[2] == "2":
                        string[2] = "0"
                        change2 = True
                        
                  if change2:
                        if old_string[1] == "0":
                              string[1] = "1"
                        elif old_string[1] == "1":
                              string[1] = "2"
                        elif old_string[1] == "2":
                              string[1] = "0"
                              change3 = True
                  if change3:
                        if old_string[0] == "0":
                            string[0] = "1"
                        elif old_string[0] == "1":
                              string[0] = "2"
                        elif old_string[0] == "2":
                              string[0] = "0"

                  count += 1
                  change2 = False
                  change3 = False

            letter = chr(count+65)
            code+= letter

      print "The Encrypted code is:"
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
      


                  
                  
