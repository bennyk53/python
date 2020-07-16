# Name: Ben Koczwara
# Date: Sept.26,2013
# Purpose: create a program that will calculate the price of a CD

print "Cost of Producing and Manufactoring a Music CD"
print "----------------------------------------------"
print
filename = "CDTracks.txt"
info = open(filename,"r")

print "Name of Music CD".ljust(40),"Cost"
print "----------------".ljust(40),"----"
print
line = info.readline().rstrip("\n")
while line != "":
      name = line.split(": ")
      print name[0].ljust(40),
      lsong = name[1].split(" ")
      num_songs = lsong[0]
      lsong.remove(lsong[0])
      price_s = float(num_songs) * .08

      total_t = 0

      for x in lsong:
            total_t += float(x)

      if total_t <= 60:
            price_t = float(total_t)*.03

      elif total_t > 60:
            price_t = float(total_t)*.02


      total_p = price_t + price_s+.45

      print "$"+str(total_p)
            
      line = info.readline().rstrip("\n")
