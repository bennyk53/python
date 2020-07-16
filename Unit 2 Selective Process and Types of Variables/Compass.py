# Name: Ben Koczwara
# Date: Sept.5,2013
# Purpose: to create a program that will tell you which direction your compass is facing by a degree

print "Compass Rose"
print "------------"
print
print "This program will tell you the direction that your compass is facing"
print "when you enter the degree"
print
again = "y"
while again == "y":
    value = True
    while value:
          degree = float(raw_input("Enter the degree of the compass: "))
          print
          if degree <= 360:
                value = False
          else:
                print "No direction avaliable"
                print
                
                
    if degree >= 348.75 and degree <= 360 or degree >= 0 and degree < 11.25:
        b = "North (N)"
    elif degree >=11.25 and degree < 33.75:
        b = "North North East (NNW)"
    elif degree >=33.75 and degree <56.25:
        b = "North East (NE)"
    elif degree >=56.25 and degree <78.75:
        b = "East North East (ENE)"
    elif degree >=78.75 and degree < 101.25:
        b = "East (E)"
    elif degree >=101.25 and degree < 123.75:
        b = "East South East (ESE)"
    elif degree >=123.75 and degree < 146.25:
        b = "South East (SE)"
    elif degree >=146.25 and degree < 168.75:
        b = "South South East (SSE)"
    elif degree >=168.75 and degree <191.25:
        b = "South (S)"
    elif degree >=191.25 and degree < 213.75:
        b = "South South West (SSW)"
    elif degree >=213.75 and degree < 236.25:
        b = "South West (SW)"
    elif degree >=236.25 and degree < 258.75:
        b = "West South West (WSW)"
    elif degree >=258.75 and degree <281.25:
        b = "West (W)"
    elif degree >=281.25 and degree < 303.75:
        b = "West North West (WNW)"
    elif degree >=303.75 and degree <326.25:
        b = "North West (NW)"
    elif degree >=326.25 and degree < 348.75:
        b = "North North West (NNW)"

    print "The compass direction is",b

    print 
    again = raw_input("Would you like to find another direction? (y/n): ").lower()
    again = again[0]
    print
    


    

