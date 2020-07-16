# Name: Ben Koczwara
# Date: Oct.22,2013
# Purpose: create a program that will print out some golf game results

print "Golf Game Application"
print "---------------------"
print

grid = [[0 for x in range(0,9)] for w in range (0,4)]
players = []
for x in range(1,5):
      name = raw_input("Enter the name of player "+str(x)+": ").capitalize()
      players.append(name)
print
for col in range(0,4):
      for row in range(0,9):
            go = False
            while not go:
                  try:
                        score = int(raw_input("Enter the score for "+players[col]+" on Hole "+str(row+1)+": "))
                        if score > 0:
                              grid[col][row] = score
                              go = True
                        else:
                              print
                              print "Not a valid score"
                              print
                  except:
                        print
                        print "Not a valid score"
                        print
      print 
print
longest = 0
for x in players:
      if len(x) > longest:
            longest = len(x)
print " ".rjust(longest),

for x in range (1,10):
      print ("Hole "+str(x)).center(7),
print

for row in range (0,4):
      print players[row].ljust(longest),
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

print players[0],len(w1),"Holes:",
for x in w1:
      print "Hole",x,
print
print players[1],len(w2),"Holes:",
for x in w2:
      print "Hole",x,
print
print players[2],len(w3),"Holes:",
for x in w3:
      print "Hole",x,
print
print players[3],len(w4),"Holes:",
for x in w4:
      print "Hole",x,
print


      


