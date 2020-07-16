# Name: Ben Koczwara
# Date: Oct.22,2013
# Purpose: create a program that will do 'matrix addition'

print "Matrix Multiplication"
print "---------------------"
print

filename = "MatrixAandB.txt"
info = open(filename,"r")

num1 = info.readline().rstrip("\n")
num1 = num1.split(" ")
rows1 = int(num1[0])
cols1 = int(num1[1])

matrix_a = [[0 for x in range (0,cols1)]for y in range (0,rows1)]

for row in range(0,rows1):
      values = info.readline().rstrip("\n")
      values = values.split(" ")
      for col in range(0,cols1):
            matrix_a[row][col] = values[col]

num2 = info.readline().rstrip("\n")
num2 = num2.split(" ")
rows2 = int(num2[0])
cols2 = int(num2[1])

matrix_b = [[0 for x in range (0,cols2)]for y in range (0,rows2)]

for row in range(0,rows2):
      values = info.readline().rstrip("\n")
      values = values.split(" ")
      for col in range(0,cols2):
            matrix_b[row][col] = values[col]
print "---" ,"---".rjust(cols1*5-1)       
for row in range (0,rows1):
      print "|",
      for col in range (0,cols1):
            print matrix_a[row][col].center(4),
      print "|"
print "---","---".rjust(cols1*5-1)

print
print "X".center(20)
print
print "---","---".rjust(cols2*5-1)
for row in range (0,rows2):
      print "|",
      for col in range (0,cols2):
            print matrix_b[row][col].center(4),
      print "|"
print "---","---".rjust(cols2*5-1)

answer = [[0 for x in range (0,cols2)]for y in range (0,rows1)]

value = cols1
for row in range (0,rows1):
      for col in range(0,cols2):
            num = 0
            for x in range (0,value):
                  multi1 = int(matrix_a[row][x])
                  multi2 = int(matrix_b[x][col])
                  num += multi1*multi2
            answer[row][col] = num

print
print "=".center(20)
print
print "---","---".rjust(cols2*5-1)
for row in range (0,rows1):
      print "|",
      for col in range (0,cols2):
            print str(answer[row][col]).center(4),
      print "|"
print "---","---".rjust(cols2*5-1)

            
            


      
            
            
            
            

