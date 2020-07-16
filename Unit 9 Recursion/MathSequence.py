# Name: Ben Koczwara
# Date: Oct.28,2013
# Purpose: to create a program that will determine a number in a math sequence

def math(n):
      if n == 1:
            return 2
      else:
            return 3*math(n-1)-1

print "Math Sequence"
print "-------------"
print
print "The following sequence is defined as follows:"
print "t(1) = 2"
print "t(n) = 3 * t(n-1) – 1, n > 1"
print
print "This program uses recursion to find the nth term of the sequence."
print
n = 1
while n > 0:
      go = False
      while not go:
            try:
                  n = int(raw_input("Enter a value for n(0 to quit): "))
                  if n >= 1:
                        value = math(n)
                        print
                        print "t("+str(n)+") =",value
                        print
                        go = True
                  elif n == 0 :
                        go = True
                  else:
                        print
                        print "Must be greater than 0"
                        print
            except:
                  print
                  print "Must be a whole number"
                  print
