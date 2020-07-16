# Name: Ben Koczwara
# Date: Sept.10,2013
# Purpose: to create a program that will give you random math questions
import random
print "Math Tutor"
print "----------"
print
print "This program will ask you 10 random math questions and give you an score"
print "out of 10"
print
again = "y"
while again == "y":
      correct = 0
      wrong = 0
      for x in range(1,11):
            mult = False
            print "Question",str(x)+":",
            num1 = random.randint(-100,100)
            num2 = random.randint(-100,100)
            sign = random.choice(["*","/","+","-"]) 

            if sign == "-":
                  check = num1 - num2
            elif sign == "+":
                  check = num1 + num2
            elif sign == "*":
                  check = num1 * num2
            elif sign == "/":
                  while num2 == 0:
                        num2 = random.randint(-100,100)
                  num1 = num1 * num2
                  check = num1 / num2
                              

            print num1,sign,num2,"=",
            going = True
            while going:
                  try:
                        answer = int(raw_input(""))
                        going = False
                  except:
                        print "Must be a whole number"
                        print "Question",str(x)+":",
                        print num1,sign,num2,"=",
                        

            if check == answer:
                  correct += 1
                  print "You are correct"
            elif check != answer:
                  wrong += 1
                  print "Sorry you are incorrect, the correct answer is",check
      print      
      print "Your score is",str(correct)+"/10 =",str(correct*10)+"%"
      print

      try_again = False
      while not try_again:
            again = raw_input("Would you like to try again? (y/n): ")
            print
            if again != "":
                  again = again[0]
                  try_again = True
            else:
                  print "You must enter something"
                  print

            
