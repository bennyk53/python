# Name: Ben Koczwara
# Date: Nov.5,2013
# Purpose: to create a program that will find the largest oil slick

def check_grid(row,col):
      global count
      if grid[row][col] == "O":
            grid[row][col] = " "
            count += 1
            
            check_grid(row+1,col)
            check_grid(row+1,col+1)
            check_grid(row+1,col-1)
            check_grid(row-1,col)
            check_grid(row-1,col+1)
            check_grid(row-1,col-1)
            check_grid(row,col+1)
            check_grid(row,col-1)

def draw_grid(grid):
      print " 0123456789012345678901234567890123456789"
      w =  0
      for x in range(0,30):
            line = ""
            line += str(w)
            for y in range(0,40):
                  line += grid[x][y]
            print line
            if w != 9:
                  w+= 1
            else:
                  w = 0

filename = "Slicks.txt"
info = open(filename,"r")

print "Oil Slick Finder"
print "----------------"
print
print "This program will find the largest oil slick"
print
grid = [[" " for x in range(0,40)]for y in range(0,30)]
coord = []
size = []

for row in range(0,30):
      line = info.readline().rstrip("\n")
      for col in range(0,40):
            grid[row][col] = line[col]

print "The original Oil Slick grid is:"
print
draw_grid(grid)
for row in range(0,30):
      for col in range(0,40):
            count = 0
            if grid[row][col] == "O":
                  check_grid(row,col)
                  coord.append([row,col])
                  size.append(count)
most = max(size)
num = size.index(most)
point = coord[num]
print
print "The largest slick is",most,"cells"
print "The uppermost, leftmost co-ordinates of the largest slick are:",point
            



      
