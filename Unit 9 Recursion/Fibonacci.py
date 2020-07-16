# Name: Ben Koczwara
# Date: Oct.28,2013
# Purpose: to create the fibonacci sequence using recursion

def fib(n):
      if n in [0,1]:
            return 1

      else:
            return fib(n-1)+fib(n-2)
      

print "Fibonacci Numbers"
print "-----------------"
print
print "This program uses recursion to find the nth Fibonacci number"
print
n = 1
while n >= 0:
      go = False
      while not go:
            try:
                  n = int(raw_input("Enter a value for n(negative number to quit): "))
                  if n >= 0:
                        value = fib(n)
                        print
                        print "F("+str(n)+") =",value
                        print
                        go = True
                  else:
                        go = True
            except:
                  print
                  print "Must be a whole number"
                  print
                  
      
      

      
