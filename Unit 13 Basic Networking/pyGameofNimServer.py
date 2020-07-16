import socket
from socket import *
import time
import random

ip = gethostbyname(gethostname())
print "The IP address is",ip

port = 21

ads = (ip,port)

server = socket(AF_INET,SOCK_STREAM)
server.bind(ads)
server.listen(5)
print "Waiting for player 1"

client1,addr = server.accept()
print "Player 1 connected from",addr
print "Waiting for player 2"

client2,addr = server.accept()
print "Player 2 connected from",addr

num_rocks = random.randint(15,30)
playing = client1

while num_rocks > 0:
      playing.send(str(num_rocks))
      taken = playing.recv(1024)
      num_rocks -= int(taken)
      playing.send(str(num_rocks))
      if num_rocks < 0:
            num_rocks = 0
      print taken,"rocks were taken.",num_rocks,"remain"
      if num_rocks > 0:
            if playing == client1:
                  playing = client2
                  waiting = client1
            else:
                  playing = client1
                  waiting = client2

loser = playing
winner = waiting

winner.send("win")
loser.send("lose")

client1.close()
client2.close()
server.close()


      


             
