# Ben Koczwara
# Dec.13,2013
# create a program that deciphers a Base Three Code

print "Bass Three Code Encryptor"
print "-------------------------"
print
print "This program will encrypt a message using Base Three Code"
print
again = "y"
while again == "y":
      message = ""
      numbers = []
      new_message = ""
      new_numbers = []
      code = raw_input("Enter the message that you wish to decipher: ").upper()
      print
      for w in code:
            
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

            numbers.append(num)
      list1 = []
      list2 = []
      list3 = []
      for i in range(0,len(numbers)):
            list1.append(numbers[i][0])
            list2.append(numbers[i][1])
            list3.append(numbers[i][2])

      master = list1+list2+list3
            
      s = 0
      f = 3
      for r in code:
            quick_list = master[s:f]
            num = ""
            for values in quick_list:
                  num += values
                  
            new_numbers.append(num)

            s += 3
            f += 3

      for nums in new_numbers:
            string = ["0","0","0"]
            count = 0
            if nums == "222":
                  count = -33
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
            message+= letter

      print "The code you wanted deciphered is:"
      print message
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
