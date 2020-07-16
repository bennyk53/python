# Name: Ben Koczwara
# Date: Oct.15,2103
# Purpose: to create a program that will count the number for days to a given date

def Day_Number(day,year,month):
      longmonths = [1,3,5,7,8,10,12]
      shortmonths = [4,6,9,11]
      if year%4 == 0 or year%400 == 0:
            feb = 29
      else:
            feb = 28

      x = 1
      days = 0
      while x <= month:
            if x in longmonths:
                  if x != month:
                        days += 31
                  else:
                        days += day
            elif x in shortmonths:
                  if x != month:
                        days += 30
                  else:
                        days += day
            else:
                  if x != month:
                        days += feb
                  else:
                        days += day

            x += 1
      return days
            
      

print "Day Counter"
print "-----------"
print
print "This program will count the number of days from the beginning of the year"
print "to a given date"
print
again = "y"
while again == "y":
      go = False
      while not go:
            try:
                  day = int(raw_input("Enter the value for the day(1-31): "))
                  month = int(raw_input("Enter the value for the month(1-12): "))
                  year = int(raw_input("Enter the value for the year: "))
                  print
                  if day <= 0 or month <= 0 or year <= 0:
                        print "You can only enter positive whole numbers"
                        print
                  elif (month == 2 and day > 28 and month%4 != 0) or day > 31:
                        print "Invalid number of days for this month"
                        print
                  elif month > 12:
                        print "You can only enter a number lower than 12 for the month"
                        print
                  else:
                        go = True
            except:
                  print
                  print "You can only enter positive whole numbers"
                  print
      

      days = Day_Number(day,year,month)

      print "The number of days from the beginning of the year is:",days
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
