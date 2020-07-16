# Name: Ben Koczwara
# Date: Oct.21,2013
# Purpose: create a program that will print out some golf game results
import random

print "Golf Game Application"
print "---------------------"
print

grid = [[0 for x in range(0,9)] for w in range (0,4)]

for row in range (0,4):
      for col in range(0,9):
            grid[row][col] = random.randint(1,9)


print "        ",

for x in range (1,10):
      print ("Hole "+str(x)).center(7),
print

for row in range (0,4):
      print "Player",row+1,
      for col in range(0,9):
            print str(grid[row][col]).center(7),
      print
print
p1 = grid[0]
p2 = grid[1]
p3 = grid[2]
p4 = grid[3]

w1 = []
w2 = []
w3 = []
w4 = []

for x in range (0,9):
      scores = []
      scores.append(p1[x])
      scores.append(p2[x])
      scores.append(p3[x])
      scores.append(p4[x])

      if scores.count(min(scores)) == 1:
            if p1[x] == min(scores):
                  w1.append(x+1)
            elif p2[x] == min(scores):
                  w2.append(x+1)
            elif p3[x] == min(scores):
                  w3.append(x+1)
            elif p4[x] == min(scores):
                  w4.append(x+1)

print "Player 1 won",len(w1),"Holes:",
for x in w1:
      print "Hole",x,
print
print "Player 2 won",len(w2),"Holes:",
for x in w2:
      print "Hole",x,
print
print "Player 3 won",len(w3),"Holes:",
for x in w3:
      print "Hole",x,
print
print "Player 4 won",len(w4),"Holes:",
for x in w4:
      print "Hole",x,
print


      


