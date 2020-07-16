# Name: Ben Koczwara
# Date: Oct.30,2013
# Purpose: to rewrite the 'Towers of Hanoi' program

def hanoi(fromPeg,toPeg,tempPeg,numDiscs,pega,pegb,pegc):
      if numDiscs == 1:
            if toPeg == "A" and fromPeg == "B":
                  pega.append(pegb.pop())
            if toPeg == "A" and fromPeg == "C":
                  pega.append(pegc.pop())
            if toPeg == "B" and fromPeg == "A":
                  pegb.append(pega.pop())
            if toPeg == "B" and fromPeg == "C":
                  pegb.append(pegc.pop())
            if toPeg == "C" and fromPeg == "A":
                  pegc.append(pega.pop())
            if toPeg == "C" and fromPeg == "B":
                  pegc.append(pegb.pop())
            print "Peg A:",
            for x in pega:
                  print x,
            print
            print "Peg B:",
            for x in pegb:
                  print x,
            print
            print "Peg C:",
            for x in pegc:
                  print x,
            print
            print
            nxt = raw_input("Press Enter to see next move")
            print
      else:
            hanoi(fromPeg, tempPeg, toPeg, numDiscs-1,pega,pegb,pegc)
            if toPeg == "A" and fromPeg == "B":
                  pega.append(pegb.pop())
            if toPeg == "A" and fromPeg == "C":
                  pega.append(pegc.pop())
            if toPeg == "B" and fromPeg == "A":
                  pegb.append(pega.pop())
            if toPeg == "B" and fromPeg == "C":
                  pegb.append(pegc.pop())
            if toPeg == "C" and fromPeg == "A":
                  pegc.append(pega.pop())
            if toPeg == "C" and fromPeg == "B":
                  pegc.append(pegb.pop())
            print "Peg A:",
            for x in pega:
                  print x,
            print
            print "Peg B:",
            for x in pegb:
                  print x,
            print
            print "Peg C:",
            for x in pegc:
                  print x,
            print
            print
            nxt = raw_input("Press Enter to see next move")
            print
            hanoi(tempPeg, toPeg, fromPeg, numDiscs-1,pega,pegb,pegc)
print "Towers of Hanoi"
print "---------------"
print
go = False
while not go:
      try:
            num = int(raw_input("Enter number of discs on peg A initially: "))
            if num > 0:
                  go = True
            else:
                  print
                  print "You need top enter a postive number"
                  print
      except:
            print
            print "You can only enter positive whole numbers"
            print
print
fPeg = "A"
tPeg = "C"
tmpPeg = "B"
pega = []
pegb = []
pegc = []
for x in range(num,0,-1):
      pega.append(x)

print "Peg A:",
for x in pega:
      print x,
print
print "Peg B:",
for x in pegb:
      print x,
print
print "Peg C:",
for x in pegc:
      print x,
print
print
nxt = raw_input("Press Enter to see next move")
print
if num < 1:
      print "Invalid number of discs"
else:
      hanoi(fPeg,tPeg,tmpPeg,num,pega,pegb,pegc)

print "Game Complete"
