# Name: Ben Koczwara
# Date: Sept.9,2013
# Purpose: To create a program that will play rock-paper-scissor
import random

def playing(choice,c_choice):
    result = ""
    adj = ""
    if choice == c_choice:
        result = "It is a tie."
        
    # player = rock
    elif choice == "Rock" and c_choice == "Paper":
        result = "You lose."
        adj = "covered"
    elif choice == "Rock" and c_choice == "Scissors":
        result = "You win."
        adj = "smashes"
        
    #player = paper
    elif choice == "Paper" and c_choice == "Scissors":
        result = "You lose."
        adj = "cut"
    elif choice == "Paper" and c_choice == "Rock":
        result = "You win."
        adj = "covers"
        
    # player= scissors
    elif choice == "Scissors" and c_choice == "Rock":
        result = "You lose."
        adj = "smashed"
    elif choice == "Scissors" and c_choice == "Paper":
        result = "You win."
        adj = "cut"
        
    return result,adj



print "Rock,Paper,Scissors"
print "-------------------"
print
print "This program will beat you in rock, paper, scissors"
print
again = "y"
while again == "y":
      name = raw_input("Enter your name: ")
      print

      player_wins = 0
      computer_wins = 0
      ties = 0

      
      while (player_wins < 2) and (computer_wins < 2):
            play = False
            while not play:
                  print name.capitalize(),
                  try:
                        choice = int(raw_input("enter your choice (1=Rock, 2=Paper, 3=Scissors): "))
                        print
                  except:
                        choice = 23
            
                  if (choice in [1,2,3]):
                        play = True
                  else:
                        print "You can only choose 1,2 or 3"
                        print
                        

            if choice == 1:
                  choice = "Rock"
            elif choice == 2:
                  choice = "Paper"
            elif choice == 3:
                  choice = "Scissors"

            c_choice = random.choice(["Rock","Paper","Scissors"])

            winner,how =  playing(choice,c_choice)
        
            if winner == "It is a tie.":
                  print name+",","you picked",choice,"so did the computer.",winner
                  print
                  ties +=1
                          
            elif winner == "You win.":
                  print name+",","your",choice,how,"the computer's",c_choice+".",winner
                  print
                  player_wins +=1
                  
            elif winner == "You lose.":
                  print name+",","your",choice,"gets",how,"by the computer's",c_choice+".",winner
                  print
                  computer_wins +=1
                  
            print name,"Wins:",player_wins
            print "Computer Wins:",computer_wins
            print "Ties:",ties
            print
                  
      if player_wins > computer_wins:
            print "Congratulations",name+",","you have won Rock Paper Scissors."
            print
      else:
            print "You lost the game of Rock Paper Scissors."
            print

      play_again = False
      while not play_again:
            again = raw_input("Would you like to play again? (y/n): ")
            print
            if again != "":
                  again = again[0]
                  play_again = True
            else:
                  print "You must enter something"
                  print
                  


            

            
            
            
      
