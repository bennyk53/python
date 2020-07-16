# Name: Ben Koczwara
# Date: Sept.5,2013
# Purpose: this program will calculate your bmi

print "BMI"
print "---"
print
print "This program will calculate your bmi"
print
again = "y"
while again == "y":
    weight = float(raw_input("Enter your weight in kilograms: "))
    height = float(raw_input("Enter your height in metres: "))
    print
    bmi = weight / (height**2)
    print u"Your BMI is",round(bmi,2),"kg/m squared"
    
    if bmi < 15:
        print "You are starving get some food"
    elif bmi >= 15 and bmi < 18.5:
        print "You are underweight eat more calories"
    elif bmi >= 18.5 and bmi <= 25:
        print "You are at an ideal BMI"
    elif bmi > 25 and bmi <= 30:
        print "You are overweight reduce your calories"
    elif bmi > 30 and bmi <= 40:
        print "You are obese get some exercise"
    else:
        print "You are morbidly obese!!!!! Get some help"
    print

    again = raw_input("Would you like to calculate another BMI? (y/n): ").lower()
    again = again[0]
    print
