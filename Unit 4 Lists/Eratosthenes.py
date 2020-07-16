# Name: Ben Koczwara
# Date: Sept.16,2013
# Purpose: to create a program that finds the prime numbers from 2 to 5000

print "Prime Numbers"
print "-------------"
print
print "This program will find all the prime numbers between 2 and 5000"
print

values = []
for x in range(2,5001):
    values.append(x)


for y in values:
    print y,
    for z in range(2,5001):
        num = y*z
        if num in values:
            values.remove(num)


        
