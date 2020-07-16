# Name: Ben Koczwara
# Date: Sept.13,2013
# Purpose: to create a program that will create a simple mad lib
import random

print "Mad Lib"
print "-------"
print
print "This program will generate a random phrase with a plural noun, verb and singular noun"
print
again = "y"
while again == "y":

    verbs = ["run","sleep","jump","flip","swim","fall","climb","pull","eat","catch"]
    p_nouns = ["Pigs","Chairs","Windows","Clocks","Computers","TVs","Leaves","Mice","Phones","Signs"]
    s_nouns = ["book","table","cow","door","light","wire","paint","key","paper","rock"]

    p_noun = random.choice(p_nouns)
    verb = random.choice(verbs)
    s_noun = random.choice(s_nouns)

    print p_noun,verb,s_noun
    print

    run_again = False
    while not run_again:
        again = raw_input("Would you like to run the program again? (y/n): ").lower()
        print
        if again != "":
                run_again = True
        else:
            print "You must enter something"
            print

    again = again[0]
