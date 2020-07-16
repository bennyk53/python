# Name: Ben Koczwara
# Date: Oct.10,2013
# Purpose: to create a program that will manage Mad Lib text files

import random

def menu():
      print "a. Display a Madlib"
      print "b. Create a new Plural Noun text file"
      print "c. Create a new Verb text file"
      print "d. Create a new Singular Noun text file"
      print "e. Add a new noun to the Plural Noun text file"
      print "f. Add a new verb to the Verb text file"
      print "g. Add a new noun to the Singular Noun text file"
      print "h. Delete a noun from the Plural Noun text file"
      print "i. Delete a verb from the Verb text file"
      print "j. Delete a noun from the Singular Noun text file"
      print "k. List the Plural Noun text file"
      print "l. List the Verb text file"
      print "m. List the Singular Noun text file"
      print "x. Exit the program"
      print
      go = False
      while not go:
            choice = raw_input("Enter your choice: ").lower()
            print
            if (ord(choice) >= 97 and ord(choice) <= 109) or (ord(choice) == 120):
                  go = True
            else:
                  print "You can only enter the letters given"
                  print

      return choice

def display_madlib():
      try:
            filename = "plural nouns.txt"
            plural_noun = open(filename,"r")
            filename = "singular nouns.txt"
            sin_noun = open(filename,"r")
            filename = "verbs.txt"
            verb = open(filename,"r")
      

            pnouns = []
            pnoun = plural_noun.readline().rstrip("\n")
            while pnoun != "":
                  pnouns.append(pnoun)
                  pnoun = plural_noun.readline().rstrip("\n")
            pnoun = random.choice(pnouns)
      
            verbs = []
            v = verb.readline().rstrip("\n")
            while v != "":
                  verbs.append(v)
                  v = verb.readline().rstrip("\n")
            v = random.choice(verbs)
            
            snouns = []
            snoun = sin_noun.readline().rstrip("\n")
            while snoun != "":
                  snouns.append(snoun)
                  snoun = sin_noun.readline().rstrip("\n")
            snoun = random.choice(snouns)
            
            print "The",pnoun,v,snoun
            print
      except:
            print "You don't have all the text files required to do this option"
            print

      plural_noun.close()
      sin_noun.close()
      verb.close()


def new_file(txt):
      filename = txt+".txt"
      info = open(filename,"w")
      info.close()
      print "The Text file",filename,"was created"
      print
      info.close()


def new_word(txt):
      try:
            filename = txt+".txt"
            info = open(filename,"r")
            word = info.readline().rstrip("\n")
            words=[]

            while word != "":
                  words.append(word)

                  word = info.readline().rstrip("\n")
            info.close()

            new = raw_input("Enter your new "+txt+": ")
            words.append(new)

            info = open(filename,"w")

            for x in words:
                  info.write(x+"\n")

            print
            print new,"was added to the text file"
            print

      except:
            print "There is no",txt,"text file"
            print
      info.close()


def del_word(txt):
      try:
            filename = txt+".txt"
            info = open(filename,"r")
            word = info.readline().rstrip("\n")
            words = []

            while word != "":
                  words.append(word)

                  word = info.readline().rstrip("\n")
            info.close()

            new = raw_input("Enter the words you wish to remove: ")
            if new in words:
                  words.remove(new)
                  info = open(filename,"w")

                  for x in words:
                        info.write(x+"\n")
                  print
                  print new,"was deleted from the text file"
                  print
            else:
                  print new,"is not in the text file"
                  print

      

      except:
            print "There is no",txt,"text file"
            print

      info.close()

def words(txt):
      try:
            filename = txt+".txt"
            info = open(filename,"r")
            word = info.readline().rstrip("\n")
            words = []

            while word != "":
                  words.append(word)

                  word = info.readline().rstrip("\n")
            info.close()

            for x in words:
                  print x
            print
      except:
            print "There is no",txt,"text file"
            print

      info.close()

      
print "Mad Lib Maintenance"
print "-------------------"
print
done = False
while not done:
      choice = menu()
      
      if choice == "a":
            display_madlib()
      elif choice == "b":
            txt = "plural nouns"
            new_file(txt)
      elif choice == "c":
            txt = "verbs"
            new_file(txt)
      elif choice == "d":
            txt = "singular nouns"
            new_file(txt)
      elif choice == "e":
            txt = "plural nouns"
            new_word(txt)
      elif choice == "f":
            txt = "verbs"
            new_word(txt)
      elif choice == "g":
            txt = "singular nouns"
            new_word(txt)
      elif choice == "h":
            txt = "plural nouns"
            del_word(txt)
      elif choice == "i":
            txt = "verbs"
            del_word(txt)
      elif choice == "j":
            txt = "singular nouns"
            del_word(txt)
      elif choice == "k":
            txt = "plural nouns"
            word(txt)
      elif choice == "l":
            txt = "verbs"
            words(txt)
      elif choice == "m":
            txt = "singular nouns"
            words(txt)
      elif choice == "x":
            done = True
            print "BYE"
      
