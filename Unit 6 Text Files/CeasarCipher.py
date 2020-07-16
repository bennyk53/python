# Name: Ben Koczwara
# Date: Sept.30,2013
# Purpose: create a program that will crack Ceasar Cipher
filename = "EncipheredCode.txt"
info = open(filename,"r")

print "Ceasar Cipher"
print "-------------"
print
print "The coded message was:",
line = info.readline().rstrip("\n")
message = ""
new_message = ""

while line != "":
      message += line+" "

      line = info.readline().rstrip("\n")

letter = ""
high = 0
alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

for x in alpha:
      occurs = message.count(x)
      
      if occurs > high:
            high = occurs 
            letter = x

num = ord(letter)

change = num - 69


for x in message:
      if x.isalpha():
            value = ord(x)
            value -= change
            if value < 65:
                  extra = 64 - value
                  value = 90 - extra
            char = chr(value)
            new_message += char
      else:
            new_message += x

print new_message
