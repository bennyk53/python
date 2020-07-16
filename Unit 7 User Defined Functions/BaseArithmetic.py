# Name: Ben Koczwara
# Date: Oct.16,2103
# Purpose: to create a program that will do some arithemtic

filename = "BaseArithmetics.txt"
info = open(filename,"r")

def base10(num1,num2,b1):
      new1 = int(num1,b1)
      new2 = int(num2,b1)
      return new1,new2
      
def finalbase(total,b2,bases):
      newtotal = ""
      while total != 0:
            num = total%b2
            num = bases[num]
            total /= b2
            newtotal += str(num)
      newtotal = newtotal[::-1]
      return newtotal

def answer(p1,num1,sign,num2,b2):
      bases = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
      new1,new2 = base10(num1,num2,b1)
      print "=",new1,"(base 10)",sign,new2,"(base 10)"
      if sign == "+":
            total = new1+new2
      elif sign == "-":
            total = new1-new2
      elif sign == "*":
            total = new1*new2
      else:
            total = new1/new2
      print "=",(total),"(base 10)"
      newtotal = finalbase(total,b2,bases)
      print "=",(newtotal),"(base",str(b2)+")"

print "Base Arithmetic"
print "---------------"
print
print "This program performs arithmetic on numbers in any base from 2 to 16"
print

q = info.readline().rstrip("\n")
while q != "":
      values = q.split(" ")
      b1 = int(values[0])
      num1 = values[1]
      sign = values[2]
      num2 = values[3]
      b2 = int(values[4])

      print " ",num1,"(base",str(b1)+")",sign,num2,"(base",str(b1)+")"

      answer(b1,num1,sign,num2,b2)
      print
      q = info.readline().rstrip("\n")
