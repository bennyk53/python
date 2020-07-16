# Name: Ben Koczwara
# Date: Oct.24,2013
# Purpose: to create the game of life

import random

def check(row,col,grid):
    up  = 0
    down = 0
    right = 0
    left = 0

    if row != 0:
        if grid[row-1][col] == "X":
            up += 1
    if row != 19:
        if grid[row+1][col] == "X":
            down += 1
        

    if col != 0:
        if grid[row][col-1] == "X":
            left += 1
        if row != 0:
            if grid[row-1][col-1] == "X":
                left += 1
        if row != 19:
            if grid[row+1][col-1] == "X":
                left += 1
            
    
    if col != 19:
        if grid[row][col+1] == "X":
            right += 1
        if row !=0 :
            if grid[row-1][col+1] == "X":
                right += 1
        if row != 19:
            if grid[row+1][col+1] == "X":
                right += 1

    total = down+up+right+left
    return total
        
        

print "Game of Life"
print "------------"
print

grid = [[ "-" for x in range (0,20)]for y in range (0,20)]

go = False
while not go:
    try:
        start = int(raw_input("How many live cells would you like to start with: "))
        print
        if start > 0 and start <= 400:
            go = True
        else:
            print "You can only enter numbers greater than 0 and less than 401"
            print
    except:
        print
        print "You can only enter whole numbers"
        print
alive = 0
while alive != start:
    col = random.randint(0,19)
    row = random.randint(0,19)

    if grid[row][col] != "X":
        grid[row][col] = "X"
        alive += 1

print "Initial Generation"
for row in range (0,20):
    for col in range(0,20):
        print grid[row][col],
    print
    
con = 1
gen = 1
while con != "q":
    print
    print "There are",alive,"live cells in the grid"
    print
    alive = 0
    con = raw_input("Press Enter to continue or Q to quit ").lower()
    if con != "q":
        print
        alive = 0
        new = [["-" for x in range (0,20)]for y in range (0,20)]
        for row in range (0,20):
            for col in range (0,20):
                around = check(row,col,grid)

                if grid[row][col] == "X" and around in [2,3]:
                    new[row][col] = "X"
                    alive += 1
                elif grid[row][col] == "X" and around > 3:
                    new[row][col] = "-"
                elif grid[row][col] == "X" and around < 2:
                    new[row][col] = "-"
                elif grid[row][col] == "-" and around == 3:
                    new[row][col] = "X"
                    alive += 1

        print "Generation",gen
        for row in range (0,20):
            for col in range(0,20):
                print new[row][col],
                grid[row][col] = new[row][col]
            print
        print
        if alive == 0:
            con = "q"
    gen += 1
    
print "Bye"
