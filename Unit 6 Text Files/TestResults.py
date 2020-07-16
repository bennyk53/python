# Name: Ben Koczwara
# Date: Sept.26,2013
# Purpose: create a program that will organize test scores

print "Result of Test 1 (Out of 65)"
print "----------------------------"
print
filename = "Test1Marks.txt"
info = open(filename,"r")

total = info.readline().rstrip("\n")
name = info.readline().rstrip("\n")
num = info.readline().rstrip("\n")
avg = 0
count = 0
fail = []
while num != "":
      percent =(float(num)/float(total))*100
      percent =  int(percent)
      avg += percent
      if percent >=95 and percent <=100:
            level = "4+"
      elif percent >=87 and percent <=94:
            level = "4"
      elif percent >=80 and percent <=86:
            level = "4-"
      elif percent >=77 and percent <=79:
            level = "3+"
      elif percent >=73 and percent <=76:
            level = "3"
      elif percent >=70 and percent <=72:
            level = "3-"
      elif percent >=67 and percent <=69:
            level = "2+"
      elif percent >=63 and percent <=66:
            level = "2"
      elif percent >=60 and percent <=62:
            level = "2-"
      elif percent >=57 and percent <=59:
            level = "1+"
      elif percent >=53 and percent <=56:
            level = "1"
      elif percent >=50 and percent <=52:
            level = "1-"
      elif percent < 50:
            level = "<1"

      if percent < 50:
            fail.append(name)
            
      print name.ljust(20),"-",str(percent)+"% Level:",level

      name = info.readline().rstrip("\n")
      num = info.readline().rstrip("\n")
      count += 1

avg = float(avg)/float(count)
print
print "Class Average:",str(round(avg,2))+"%"
print
print "Students with a Percentage Less than 50"
print "---------------------------------------"
for names in fail:
      print names
