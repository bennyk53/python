# Name: Ben Koczwara
# Date: Sept.18,2013
# Purpose: to create a program that will tell you the angle between the minute and second hand on a clock
import math
print "Clock Arms"
print "----------"
print
print "This program will tell you the angle between the minutes and seconds hands"
print "at a given time"
print
again = "y"
while again == "y":
      go = False
      while not go:
            time = raw_input("Enter the time in the format HH:MM:SS - ")


            if len(time) == 8:
                  if time[2]== ":" and time[5] == ":":
                        check = time.replace(":","")
                        
                        if check.isdigit():
                              go = True
                        else:
                              print "The number must be in the format 00:00:00"
                  else:
                        print "The number must be in the format 00:00:00"
            else:
                  print "The number must be in the format 00:00:00"
            print
                  
                  

      hour = int(time[:2])
      mins = int(time[3:5])
      sec = int(time[6:])

      hour_hand = (hour*30)+(mins*0.5)+(sec*(.5/60))
      min_hand = (mins*6)+(sec*.1)

      angle = hour_hand - min_hand

      if angle < 0:
            angle *= -1

      if angle > 180:
            angle = 360-angle

      ddd = int(angle)
      mm = (angle - int(angle))*60
      ss = math.floor(60*(mm - int(mm)))
      
      print str(int(ddd))+":"+str(int(mm))+":"+str(int(ss))
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
