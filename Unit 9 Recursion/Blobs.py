# Name: Ben Koczwara
# Date: Oct.31,2013
# Purpose: to erase blobs designated by the user

def delete_blob(row,col):
      if grid[row][col] == "*":
            grid[row][col] = " "
            delete_blob(row+1,col)
            delete_blob(row-1,col)
            delete_blob(row,col+1)
            delete_blob(row,col-1)

def draw_grid(grid):
      print " 012345678901234567890123456789"
      w =  0
      for x in range(0,20):
            line = ""
            line += str(w)
            for y in range(0,30):
                  if grid[x][y] == "-":
                        line += " "
                  else:
                        line += grid[x][y]
            print line
            if w != 9:
                  w+= 1
            else:
                  w = 0

print
      

filename = "Blobs.txt"
info = open(filename,"r")

print "Blob Removal"
print "------------"
print
print "This program will erase the blob specified by the user from the grid."
print
grid = [[" " for x in range(0,30)]for y in range(0,20)]

for row in range(0,20):
      line = info.readline().rstrip("\n")
      for col in range(0,30):
            grid[row][col] = line[col]
            

again = "y"
draw_grid(grid)
print
while again == "y":
      
      row = int(raw_input("Enter the row # of the blob: "))
      col = int(raw_input("Enter the column # of the blob: "))
      if grid[row][col] == "*":
            delete_blob(row,col)
            draw_grid(grid)
      else:
            print "There is not a blob at that location"
            print
      
      run_again = False
      while not run_again:
            again = raw_input("Would you like to remove another blob (y/n): ").lower()
            if again != "":
                  run_again = True
            else:
                  print "You must enter something"

      again = again[0]
      print 
