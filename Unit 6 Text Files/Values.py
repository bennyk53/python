# Name: Ben Koczwara
# Date: Sept.26,2013
# Purpose: create a program that will find the number of variables, average, highest and lowest value

filename = "Values.txt"
info = open(filename,"r")

print "Information about 'Values.txt'"
print "------------------------------"
print
print "This program will tell you the number of values, the average, the highest"
print "and lowest numbers in the text file Values.txt"
print
total = 0
num = info.readline().rstrip("\n")
values = []
while num != "":
      num = int(num)
      total += num
      values.append(num)
      num = info.readline().rstrip("\n")

print "Number of values:",len(values)
print "Average of values:",round(float(total)/float(len(values)),2)
print "Lowest Value:",min(values)
print "Highest Value:",max(values)
      
