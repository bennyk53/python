# Name: Ben Koczwara
# Date: Oct.28,2013
# Purpose: to create a program that will determine is the word or phrase is a palindrome

def palindrome(word,x,new):
      while 1:
            try:
                  if word[x].isalpha():
                        new += word[x]
                        return palindrome(word,x+1,new)
                  else:
                         word = word.replace(word[x],"")
            except:
                  if word == new[::-1]:
                        return " "
                  else:
                        return " NOT "
                  
                  


print "Palindrome"
print "----------"
print
print "This program uses recursion to determine if a word or phrase is a palindrome."
print
again = "y"
while again == "y":
      x = 0
      new = ""
      o_word = raw_input("Enter a word or phrase: ")
      word = o_word.lower()
      print
      new = palindrome(word,x,new)
      print o_word,"is"+new+"a palindrome"
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

      
      
