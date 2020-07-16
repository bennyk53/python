# Name: Ben Koczwara
# Date: Sept.5,2013
# Purpose: this program will find the combination of change

print "Change Maker"
print "------------"
print
print "This progaram will determine the combination for values under a dollar"
print

again = "y"
while again == "y":
    money = int(raw_input("Enter the amount of money in cents under 100: "))
    print
    print money,"cents requires:",

    quarters = money // 25
    if quarters > 1:
        q = "quarters"
    else:
        q = "quarter"
        
    money = money % 25
    dimes = money // 10
    if dimes > 1:
        d = "dimes"
    else:
        d = "dime"
        
    money = money % 10
    nickels = money // 5
    if nickels > 1:
        n = "nickels"
    else:
        n = "nickel"
        
    money = money % 5
    pennies = money
    if pennies >1:
        p = "pennies"
    else:
        p = "penny"

    if quarters > 0:
        print quarters,q,

    if dimes > 0:
        print dimes,d,

    if nickels > 0:
        print nickels,n,
        
    if pennies > 0:
        print pennies,p,

    print
    print

    answer = False
    while not answer:
          again = raw_input("Would you like to find another change combination? (y/n): ").lower()
          print
          if again != "" and (again[0] == "n" or again[0] == "y"):
                answer = True
          else:
                print "You must enter yes or no"
                print
    again = again[0]


    
    

        

        
        
