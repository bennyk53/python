import pygame, sys
from pygame import *
import random
import os
import time

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow = (255,255,0)
purple = (153,0,204)
green = (0,255,0)
pink = (255,51,255)
blue = (0,0,255)

#draw big grid
def big_grid(screen):
    
    #border
    pygame.draw.line(screen,black,(150,50),(650,50),7)
    pygame.draw.line(screen,black,(150,50),(150,550),7)
    pygame.draw.line(screen,black,(650,50),(650,550),7)
    pygame.draw.line(screen,black,(150,550),(650,550),7)

    #divders
    pygame.draw.line(screen,black,((150 + (500/3)),50),((150 + (500/3)),550),7)
    pygame.draw.line(screen,black,((650 - (500/3)),50),((650 - (500/3)),550),7)
    pygame.draw.line(screen,black,(150 , (50 + (500/3))),(650,(50 + (500/3))),7)
    pygame.draw.line(screen,black,(150 , (550 - (500/3))),(650,(550 - (500/3))),7)

#draw small grid
def small_grid(screen,int_x,int_y,pos_x,pos_y):
    x = int_x
    y = int_y
    while y < (int_y + (float(500)/float(3))):
        while x < (int_x+ (float(500)/float(3))):
            pygame.draw.rect(screen,black,(x,y,(500/9),(500/9)),2)

            if (pos_x >= x and pos_x < (x +(float(500)/float(9)))) and (pos_y >= y and pos_y < (y + (float(500)/float(9)))):
                pygame.draw.rect(screen,green,(x,y,(500/9),(500/9)),3)
            

            x += (float(500)/float(9))

        y += (float(500)/float(9))
        x = int_x

#easy puzzle boards and solutions
def easy1():
    easy1_s = [[1,2,'','',9,'','',3,6],
         [6,'',5,4,'',1,9,'',8],
         ['',7,9,'',6,'',4,5,''],
         ['',4,'','',5,'','',9,''],
         [9,'',3,7,8,2,1,'',5],
         ['',5,'','',1,'','',6,''],
         ['',1,6,'',4,'',2,7,''],
         [4,'',7,6,'',9,5,'',3],
         [5,9,'','',3,'','',8,4]
         ]

    easy1_b =[['','',4,8,'',5,7,'',''],
         ['',3,'','',7,'','',2,''],
         [8,'','',2,'',3,'','',1],
         [7,'',1,3,'',6,8,'',2],
         ['',6,'','','','','',4,''],
         [2,'',8,9,'',4,3,'',7],
         [3,'','',5,'',8,'','',9],
         ['',8,'','',2,'','',1,''],
         ['','',2,1,'',7,6,'','']
         ]

    return easy1_s,easy1_b

def easy2():
    easy2_s = [[6,'','',2,5,8,'','',3],
               ['',5,7,3,4,9,1,8,''],
               ['',9,3,'','','',4,2,''],
               [3,8,'','','','','',4,1],
               [1,4,'','',9,'','',3,7],
               [7,2,'','','','','',5,9],
               ['',6,8,'','','',9,1,''],
               ['',7,1,9,2,4,3,6,''],
               [9,'','',1,8,6,'','',4]
               ]

    easy2_b = [['',1,4,'','','',7,9,''],
               [2,'','','','','','','',6],
               [8,'','',6,7,1,'','',5],
               ['','',9,7,6,5,2,'',''],
               ['','',5,8,'',2,6,'',''],
               ['','',6,4,1,3,8,'',''],
               [4,'','',5,3,7,'','',2],
               [5,'','','','','','','',8],
               ['',3,2,'','','',5,7,'']
               ]

    return easy2_s,easy2_b

def easy3():
    easy3_s = [[8,'','','',7,'','','',2],
               ['',2,4,8,3,6,9,1,''],
               ['',6,'','',4,'','',8,''],
               ['',1,5,6,8,4,7,9,''],
               [4,'','','',1,'','','',8],
               ['',7,8,5,2,3,4,6,''],
               ['',5,'','',6,'','',7,''],
               ['',8,9,7,5,1,2,3,''],
               [1,'','','',9,'','','',6]
               ]

    easy3_b = [['',9,3,1,'',5,6,4,''],
               [7,'','','','','','','',5],
               [5,'',1,2,'',9,3,'',7],
               [2,'','','','','','','',3],
               ['',3,6,9,'',7,5,2,''],
               [9,'','','','','','','',1],
               [3,'',2,4,'',8,1,'',9],
               [6,'','','','','','','',4],
               ['',4,7,3,'',2,8,5,'']
               ]
    return easy3_s,easy3_b
    
#medium puzzle boards and solutions
def med1():
      med1_s = [['',3,'',1,7,8,'',5,''],
               ['','',8,'',9,'',1,4,3],
               [9,2,'',3,4,'',6,7,''],
               ['',9,'','','','','',2,5],
               ['',1,2,'',6,9,'',8,4],
               [8,4,'',7,2,3,9,1,6],
               [1,'','',6,5,7,'','',2],
               [2,'',7,8,3,4,5,9,''],
               ['',5,'',9,1,2,8,'','']
               ]

      med1_b = [[4,'',6,'','','',2,'',9],
               [5,7,'',2,'',6,'','',''],
               ['','',1,'','',5,'','',8],
               [6,'',3,4,8,1,7,'',''],
               [7,'','',5,'','',3,'',''],
               ['','',5,'','','','','',''],
               ['',8,9,'','','',4,3,''],
               ['',6,'','','','','','',1],
               [3,'',4,'','','','',6,7]
               ]
      
      return med1_s,med1_b

def med2():
      med2_s = [[1,6,'',7,'','',8,4,5],
               ['',8,9,5,'',6,7,'',2],
               ['','',5,8,1,4,3,9,6],
               [6,'',2,'',4,9,5,7,''],
               [9,'',8,'','','',2,'',4],
               ['',4,7,2,5,'',9,'',1],
               [8,2,6,9,7,1,4,'',''],
               [7,'',1,4,'',5,6,2,''],
               [5,9,4,'','',3,'',8,7]
               ]

      med2_b = [['','',3,'',9,2,'','',''],
               [4,'','','',3,'','',1,''],
               [2,7,'','','','','','',''],
               ['',1,'',3,'','','','',8],
               ['',5,'',1,6,7,'',3,''],
               [3,'','','','',8,'',6,''],
               ['','','','','','','',5,3],
               ['',3,'','',8,'','','',9],
               ['','','',6,2,'',1,'','']
               ]
      
      return med2_s,med2_b

def med3():
      med3_s = [[4,'',8,5,'',7,9,'',2],
               ['','',9,2,'',6,1,'',''],
               [1,2,'','','','','',5,7],
               [5,7,'',4,6,9,'',2,1],
               ['','','',8,5,3,'','',''],
               [8,6,'',7,2,1,'',9,3],
               [3,4,'','','','','',8,9],
               ['','',7,3,'',2,4,'',''],
               [2,'',5,1,'',8,7,'',6]
               ]

      med3_b = [['',3,'','',1,'','',6,''],
               [7,5,'','',3,'','',4,8],
               ['','',6,9,8,4,3,'',''],
               ['','',3,'','','',8,'',''],
               [9,1,2,'','','',6,7,4],
               ['','',4,'','','',5,'',''],
               ['','',1,6,7,5,2,'',''],
               [6,8,'','',9,'','',1,5],
               ['',9,'',4,'','',3,'','']
               ]
      
      return med3_s,med3_b

#hard puzzle boards and solutions
def hard1():
      hard1_s = [[2,3,'','','',4,9,6,2],
               [4,'',5,3,2,'',1,7,8],
               ['',8,9,6,7,1,'',4,5],
               ['',2,3,'',9,6,'',8,4],
               ['',1,4,2,'',7,'',5,9],
               [7,'',6,8,4,'',2,1,3],
               [3,5,'','','',2,'',9,1],
               [6,4,2,9,1,8,5,'',7],
               [2,'',5,1,'',8,7,'',6]
               ]

      hard1_b = [['','',7,5,8,'','','',''],
               ['',6,'','','',9,'','',''],
               [2,'','','','','',3,'',''],
               [5,'','',1,'','',7,'',''],
               [8,'','','',3,'',6,'',''],
               ['',9,'','','',5,'','',''],
               ['','',8,7,6,'',4,'',''],
               ['','','','','','','',3,''],
               ['','','','','','','',2,6]
               ]
      
      return hard1_s,hard1_b

def hard2():
      hard2_s = [[2,7,5,3,9,6,4,'',''],
               [8,4,'',1,5,2,9,3,7],
               ['',9,1,'','','',6,2,5],
               [1,'','',9,4,7,3,5,''],
               [9,6,7,'','','',2,1,4],
               ['',3,4,6,2,1,'','',8],
               [7,5,8,'','','',1,4,''],
               [6,2,3,4,1,8,'',7,9],
               ['','',9,7,3,5,8,6,2]
               ]

      hard2_b = [['','','','','','','',8,1],
               ['','',6,'','','','','',''],
               [3,'','',8,7,4,'','',''],
               ['',8,2,'','','','','',6],
               ['','','',5,8,3,'','',''],
               [5,'','','','','',7,9,''],
               ['','','',2,6,9,'','',3],
               ['','','','','','',5,'',''],
               [4,1,'','','','','','','']
               ]
      
      return hard2_s,hard2_b

def hard3():
      hard3_s = [[3,'',9,'',6,'',8,'',7],
               ['',2,4,7,9,8,1,3,''],
               [8,6,7,'',5,'',9,2,4],
               ['',3,'',2,1,9,'',6,''],
               [1,9,6,8,4,5,2,7,3],
               ['',4,'',6,3,7,'',1,''],
               [4,5,3,'',2,'',7,8,1],
               ['',8,1,5,7,4,3,9,''],
               [9,'',2,'',8,'',6,'',5]
               ]

      hard3_b = [['',1,'',4,'',2,'',5,''],
               [5,'','','','','','','',6],
               ['','',3,'',1,'','','',''],
               [7,'',5,'','','',4,'',8],
               ['','','','','','','','',''],
               [2,'',8,'','','',5,'',9],
               ['','','',9,'',6,'','',''],
               [6,'','','','','','','',2],
               ['',7,'',1,'',3,'',4,'']
               ]
      
      return hard3_s,hard3_b

#seeing which number is enter and wait until valid key is entered
def pause():
    while 1: 
        e = pygame.event.wait()
        if e.type == KEYDOWN:
            if e.key == K_1 or e.key == K_KP1:
                entered = 1
                return entered
            if e.key == K_2 or e.key == K_KP2:
                entered = 2
                return entered
            if e.key == K_3 or e.key == K_KP3:
                entered = 3
                return entered
            if e.key == K_4 or e.key == K_KP4:
                entered = 4
                return entered
            if e.key == K_5 or e.key == K_KP5:
                entered = 5
                return entered
            if e.key == K_6 or e.key == K_KP6:
                entered = 6
                return entered
            if e.key == K_7 or e.key == K_KP7:
                entered = 7
                return entered
            if e.key == K_8 or e.key == K_KP8:
                entered = 8
                return entered
            if e.key == K_9 or e.key == K_KP9:
                entered = 9
                return entered
            if e.key == K_BACKSPACE:
                entered = ''
                return entered
            
            
#drawint numbers
def drawing(puzzle_b,puzzle_e,screen,diff):

    y = 60
    
    for z in range(0,9):
        count = 0
        for numbers in puzzle_b[z]:
            x = 165

            x += ((float(500)/float(9))*count)
            
            
            num = number_font.render(str(numbers),True,black)
            screen.blit(num,[x,y])
            

            count +=1

        y += float(500)/float(9)

    y = 60
    
    for z in range(0,9):
        count = 0
        for numbers in puzzle_e[z]:
            x = 165

            x += ((float(500)/float(9))*count)
            
            if diff == "easy":
                  if numbers == puzzle_s[z][count]:
                        num = number_font.render(str(numbers),True,purple)
                        screen.blit(num,[x,y])
                  else:
                        num = number_font.render(str(numbers),True,red)
                        screen.blit(num,[x,y])
            else:
                  num = number_font.render(str(numbers),True,purple)
                  screen.blit(num,[x,y])
            

            count +=1

        y += float(500)/float(9)


def adding_numbers(int_x,int_y,pos_x,pos_y,col,row):

    x = int_x
    y = int_y

    while row != 9 :
        col = 0                   
        x = int_x
        while col != 9 :

            if (pos_x > x and pos_x < (x +(float(500)/float(9)))) and (pos_y > y and pos_y < (y +(float(500)/float(9)))):
                return col,row
            
            

            x += (float(500)/float(9))
            col += 1
        y += (float(500)/float(9))
        row +=1

#difficulty selection
def profile_screen(event,pos_x,pos_y,diff,start,player_name):
                
    screen.fill(black)
    game = title_font.render("SUDOKU",True,pink)
    screen.blit(game,[250,100])
    easy = number_font.render("EASY",True,white)
    screen.blit(easy,[320,200])
    med = number_font.render("MEDIUM",True,white)
    screen.blit(med,[300,300])
    hard = number_font.render("HARD",True,white)
    screen.blit(hard,[320,400])
    home = number_font.render("HOME",True,white)
    screen.blit(home,[15,550])

    if (pos_x >= 320 and pos_x <=415) and (pos_y >= 200 and pos_y <= 230):
        easy = number_font.render("EASY",True,green)
        screen.blit(easy,[320,200])
        if event.type == pygame.MOUSEBUTTONDOWN:
            diff = "easy"

    if (pos_x >= 300 and pos_x <=435) and (pos_y >= 300 and pos_y <= 330):
        med = number_font.render("MEDIUM",True,yellow)
        screen.blit(med,[300,300])
        if event.type == pygame.MOUSEBUTTONDOWN:
            diff = "med"

    if (pos_x >= 320 and pos_x <=415) and (pos_y >= 400 and pos_y <= 430):
        hard = number_font.render("HARD",True,red)
        screen.blit(hard,[320,400])
        if event.type == pygame.MOUSEBUTTONDOWN:
            diff = "hard"
    
    if (pos_x >= 15 and pos_x <=115) and (pos_y >= 550 and pos_y <= 580):
        home = number_font.render("HOME",True,blue)
        screen.blit(home,[15,550])
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = -2
            player_name = []

    return diff,start,player_name

#Main menu for program to see instructions and manage profiles
def home_screen(event,pos_x,pos_y,start,delete):
    screen.fill(black)
    game = title_font.render("SUDOKU",True,pink)
    screen.blit(game,[250,100])

    begin = number_font.render("NEW/LOAD PROFILE",True,white)
    screen.blit(begin,[205,200])
    delete_choice = number_font.render("DELETE PROFILE",True,white)
    screen.blit(delete_choice,[225,300])
    instruct = number_font.render("INSTRUCTIONS",True,white)
    screen.blit(instruct,[240,400])
    stop = number_font.render("QUIT",True,white)
    screen.blit(stop,[325,500])

    if (pos_x >= 205 and pos_x <=550) and (pos_y >= 200 and pos_y <= 230):
        begin = number_font.render("NEW/LOAD PROFILE",True,blue)
        screen.blit(begin,[205,200])
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = -1

    if (pos_x >= 225 and pos_x <=520) and (pos_y >= 300 and pos_y <= 330):
        delete_choice = number_font.render("DELETE PROFILE",True,blue)
        screen.blit(delete_choice,[225,300])
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = -1
            delete = True

    if (pos_x >= 240 and pos_x <=505) and (pos_y >= 400 and pos_y <= 430):
        instruct = number_font.render("INSTRUCTIONS",True,blue)
        screen.blit(instruct,[240,400])
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = -3

    if (pos_x >= 325 and pos_x <=410) and (pos_y >= 500 and pos_y <= 530):
        stop = number_font.render("QUIT",True,blue)
        screen.blit(stop,[325,500])
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = ""

    return start,delete

#instructions on sudoku
def instruction_screen1(event,pos_x,pos_y,start):
    screen.fill(black)
    heading = number_font.render("INSTRUCTIONS",True,pink)
    screen.blit(heading,[275,20])

    i1 = number_font.render("In sudoku the objective is to fill the squares",True,white)
    screen.blit(i1,[10,80])
    i2 = number_font.render("with the numbers 1-9. The trick is you can only",True,white)
    screen.blit(i2,[10,110])
    i3 = number_font.render("have one of each number per row, per column",True,white)
    screen.blit(i3,[10,140])
    i4 = number_font.render("and per large square.",True,white)
    screen.blit(i4,[10,170])

    back = number_font.render("HOME",True,white)
    screen.blit(back,[15,550])

    next_pg = number_font.render("NEXT",True,white)
    screen.blit(next_pg,[690,550])

    example = pygame.image.load("ex.png")
    screen.blit(example,[230,210])

    if (pos_x >= 15 and pos_x <=115) and (pos_y >= 550 and pos_y <= 580):
        back = number_font.render("HOME",True,blue)
        screen.blit(back,[15,550])
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = -2
            
    if (pos_x >= 690 and pos_x <=790) and (pos_y >= 550 and pos_y <= 580):
        next_pg = number_font.render("NEXT",True,blue)
        screen.blit(next_pg,[690,550])
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = -3.1
    

    return start

#instructions on how to intertact with the program
def instruction_screen2(event,pos_x,pos_y,start):
    screen.fill(black)
    heading = number_font.render("INSTRUCTIONS",True,pink)
    screen.blit(heading,[275,20])
    i1 = number_font.render("To interact with the puzzle you will need to",True,white)
    screen.blit(i1,[10,80])
    i2 = number_font.render("use the mouse and keyboard. When you click",True,white)
    screen.blit(i2,[10,110])
    i3 = number_font.render("on a square it will be selected. Once it is",True,white)
    screen.blit(i3,[10,140])
    i4 = number_font.render("selected you use the number keys (or keypad)",True,white)
    screen.blit(i4,[10,170])
    i5 = number_font.render("to enter the desired number. You can delete",True,white)
    screen.blit(i5,[10,200])
    i6 = number_font.render("an enter number by pressing backspace.",True,white)
    screen.blit(i6,[10,230])

    back = number_font.render("HOME",True,white)
    screen.blit(back,[15,550])
    next_pg = number_font.render("NEXT",True,white)
    screen.blit(next_pg,[690,550])
    last_pg = number_font.render("BACK",True,white)
    screen.blit(last_pg,[580,550])

    pic1 = pygame.image.load("mouse.png")
    screen.blit(pic1,[100,300])

    pic2 = pygame.image.load("keys.png")
    screen.blit(pic2,[200,300])

    pic3 = pygame.image.load("backspace.png")
    screen.blit(pic3,[450,300])

    if (pos_x >= 15 and pos_x <=115) and (pos_y >= 550 and pos_y <= 580):
        back = number_font.render("HOME",True,blue)
        screen.blit(back,[15,550])
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = -2
            
    if (pos_x >= 690 and pos_x <=780) and (pos_y >= 550 and pos_y <=580):
        next_pg = number_font.render("NEXT",True,blue)
        screen.blit(next_pg,[690,550])
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = -3.2

    if (pos_x >= 580 and pos_x <=680) and (pos_y >= 550 and pos_y <= 580):
        next_pg = number_font.render("BACK",True,blue)
        screen.blit(next_pg,[580,550])
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = -3

    return start

#information about profiles and their purpose
def instruction_screen3(event,pos_x,pos_y,start):
    screen.fill(black)
    heading = number_font.render("INSTRUCTIONS",True,pink)
    screen.blit(heading,[275,20])

    i1 = number_font.render("Your profile is used to ensure that you do not",True,white)
    screen.blit(i1,[10,80])
    i2 = number_font.render("do the same puzzles for each difficulty. Your",True,white)
    screen.blit(i2,[10,110])
    i3 = number_font.render("profile will keep track of what puzzles you have",True,white)
    screen.blit(i3,[10,140])
    i4 = number_font.render("completed. Once you have completed all the puzzles",True,white)
    screen.blit(i4,[10,170])
    i5 = number_font.render("at a certain difficulty it will reset so you start",True,white)
    screen.blit(i5,[10,200])
    i6 = number_font.render("again.",True,white)
    screen.blit(i6,[10,230])

    back = number_font.render("HOME",True,white)
    screen.blit(back,[15,550])
    
    last_pg = number_font.render("BACK",True,white)
    screen.blit(last_pg,[690,550])

    if (pos_x >= 15 and pos_x <=115) and (pos_y >= 550 and pos_y <= 580):
        back = number_font.render("HOME",True,blue)
        screen.blit(back,[15,550])
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = -2

    if (pos_x >= 330 and pos_x <=480) and (pos_y >= 550 and pos_y <=580):
        credit_screen = number_font.render("CREDITS",True,white)
        screen.blit(credit_screen,[330,550])
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = ":)"

    if (pos_x >= 690 and pos_x <=780) and (pos_y >= 550 and pos_y <=580):
        last_pg = number_font.render("BACK",True,blue)
        screen.blit(last_pg,[690,550])
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = -3.1

    return start
    
#draw profile accepting screen
def profile():
    limit = number_font.render("Your profile can only be up to 7 Characters",True,white)
    screen.blit(limit,[50,50])
    name = number_font.render("Enter your profile:",True,white)
    screen.blit(name,[100,150])

#credits screen
def secret_screen(event,pos_x,pos_y,start,s_x,s_y,direct):
    screen.fill(black)
    creator = title_font.render("Created by Ben Koczwara",True,white)
    screen.blit(creator,[10,50])

    s = pygame.image.load("superman logo.png")
    screen.blit(s,[200,200])
    
    udoku = title_font.render("udoku",True,white)
    screen.blit(udoku,[350,280])
    
    pic = pygame.image.load("superman"+direct+".png")
    screen.blit(pic,[s_x,s_y])

    if direct == "r":
        s_x += 5
        if s_x == 550:
            direct = "u"
            
    elif direct == "l":
        s_x -= 5
        if s_x == -50:
            direct = "d"
            
    elif direct == "u":
        s_y -= 5
        if s_y == -85:
            direct = "l"
            
    elif direct == "d":
        s_y += 5
        if s_y == 300:
            direct = "r"

            
            

    back = number_font.render("HOME",True,white)
    screen.blit(back,[15,550])

    if (pos_x >= 15 and pos_x <=115) and (pos_y >= 550 and pos_y <= 580):
        back = number_font.render("HOME",True,blue)
        screen.blit(back,[15,550])
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = -2

    return start,direct,s_x,s_y


    
    

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode([800,600])
number_font = pygame.font.Font(None,50)
title_font = pygame.font.Font(None,88)
pygame.display.set_caption("SUDOKU")
up = 0

screen.fill(black)
diff = ""
start = -2
count = 1
new = True
delete = False
completed = []
player_name = []
done = False
once = True
check = 0
s_x = 0
s_y = 300
direct = "r"
# main loop
while not done:
    mouse = pygame.mouse.get_pos()
    pos_x = mouse[0]
    pos_y = mouse[1]

    if start == ":)":
        start,direct,s_x,s_y = secret_screen(event,pos_x,pos_y,start,s_x,s_y,direct)
    
    for event in pygame.event.get():
        if event.type == QUIT: 
            done = True
            pygame.quit()
            sys.exit()

        if start == "":
            done = True
            pygame.quit()


        elif start == -2:
            player_name = []
            start,delete = home_screen(event,pos_x,pos_y,start,delete)

        elif start == -3:
            start = instruction_screen1(event,pos_x,pos_y,start)
            
        elif start == -3.1:
            start = instruction_screen2(event,pos_x,pos_y,start)

        elif start == -3.2:
            start = instruction_screen3(event,pos_x,pos_y,start)
        
        elif start == -1:
            screen.fill(black)
            screen_name = ""
            profile()
            x = 400
            y = 150
            #reciving profile name to delete/create/load
            if event.type == KEYDOWN and up == 0:
                up = 1
    
                if event.key == pygame.K_RETURN:
                    if len(player_name) > 0 and not delete :
                        start = 0
                    elif len(player_name) > 0 and delete:
                        start = "x"
                        delete = False
                        
                elif event.key == pygame.K_SPACE:
                    player_name.append(" ")
                elif event.key == pygame.K_BACKSPACE:
                    if len(player_name) > 0:
                        del player_name[-1]
                else:
                    if len(player_name) < 7:
                        keyname = pygame.key.name(event.key)

                        if len(keyname) == 1:
                            if len(player_name) == 0:
                                player_name.append(keyname.upper())
                            else:
                                player_name.append(keyname)
                        else:
                            pass

            if event.type == KEYUP:
                up = 0

            for letters in player_name:

                screen_name += letters

            show = number_font.render(screen_name,True,white)
            screen.blit(show,[x,y])
            home = number_font.render("HOME",True,white)
            screen.blit(home,[15,550])

            if (pos_x >= 15 and pos_x <=115) and (pos_y >= 550 and pos_y <= 580):
                home = number_font.render("HOME",True,blue)
                screen.blit(home,[15,550])
                if event.type == pygame.MOUSEBUTTONDOWN:
                    start = -2
                    
        #delete message or no such file exisit
        elif start == "x":
            try:
                if check == 0:
                    os.remove(screen_name+".txt")
                    check = 1
                screen.fill(black)
                delete_msg = number_font.render(screen_name+" was deleted",True,white)
                screen.blit(delete_msg,[235,250])
            except:
                screen.fill(black)
                cant_delete = number_font.render(screen_name+" doesn't exist",True,white)
                screen.blit(cant_delete,[235,250])

            con = number_font.render("PRESS ENTER TO CONTINUE",True,white)
            screen.blit(con,[150,400])

            if event.type == KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start = -2
                    check = 0
                

        elif start == 0:
            diff,start,player_name = profile_screen(event,pos_x,pos_y,diff,start,player_name)
            #checking the text file for completed puzzles
            try:
                filename = screen_name+".txt"
                info = open(filename,"r")
                complete = info.readline().rstrip("\n")
                if once:
                    while complete != "":
                        completed.append(complete)
                        complete = info.readline().rstrip("\n")
                    once = False
            except:
                filename = screen_name+".txt"
                info = open(filename,"w")

            info.close()
            #select puzzle
            if diff in ["easy","med","hard"]:
                while 1:
                    puzzle_num = random.choice([1,2,3])
                    if diff+str(puzzle_num) not in completed:
                        start = 1
                        count = 1
                        break
                    #if all puzzles for a difficulty are completed reset all of those puzzles (remove from text file)
                    elif [(diff+str(1)) and (diff+str(2)) and (diff+str(3))] in completed:
                        completed.remove((diff+str(1)))
                        completed.remove(diff+str(2))
                        completed.remove(diff+str(3))

        elif start == 1:

            if diff == "easy":
                if puzzle_num == 1:
                    puzzle_s,puzzle_b = easy1()
                elif puzzle_num == 2:
                    puzzle_s,puzzle_b = easy2()
                elif puzzle_num == 3:
                    puzzle_s,puzzle_b = easy3()

            elif diff == "med":
                if puzzle_num == 1:
                    puzzle_s,puzzle_b = med1()
                elif puzzle_num == 2:
                    puzzle_s,puzzle_b = med2()
                elif puzzle_num == 3:
                    puzzle_s,puzzle_b = med3()

            elif diff == "hard":
                if puzzle_num == 1:
                    puzzle_s,puzzle_b = hard1()
                elif puzzle_num == 2:
                    puzzle_s,puzzle_b = hard2()
                elif puzzle_num == 3:
                    puzzle_s,puzzle_b = hard3()
                    
                    
            
            if new:
                puzzle_e = [['' for x in range (0,9)]for z in range (0,9)]
                new = False
                
            #if mouse is pressed, take number and add it to the list of entered numbers and draw grid and numbers
            if event.type == pygame.MOUSEBUTTONDOWN and not ((pos_x > 10 and pos_x < 105 ) and (pos_y > 550 and pos_y < 580 ))  and ((pos_x > 150 and pos_x < 650) and (pos_y >50 and pos_y < 550)):
                number = pause()
                
                x = 150
                y = 50
                row = 0
                col = 0
                
                try:
                      col,row = adding_numbers(x,y,pos_x,pos_y,col,row)
                      if puzzle_b[row][col] == "":
                
                            puzzle_e[row].pop(col)
                            puzzle_e[row].insert(col,number)
                except:
                      print

            #draw grid
            screen.fill(white)
            big_grid(screen)
            x = 150
            y = 50
            while y < 550:
                while x < 600:
                    small_grid(screen,x,y,pos_x,pos_y)

                    x += (float(500)/float(3))
                    
                y += (float(500)/float(3))
                x = 150
                
            #draw numbers
            drawing(puzzle_b,puzzle_e,screen,diff)
            
            home = number_font.render("HOME",True,black)
            screen.blit(home,[15,550])
            if (pos_x >= 15 and pos_x <=115) and (pos_y >= 550 and pos_y <= 580):
                home = number_font.render("HOME",True,blue)
                screen.blit(home,[15,550])
                if event.type == pygame.MOUSEBUTTONDOWN:
                    start = 0
                    diff = ""
                    new = True
                    
            num1 = []
            num2 = []
            for a in puzzle_s:
                for b in a:
                    if str(b).isdigit():
                        num1.append(b)

            for a in puzzle_e:
                for b in a:
                    if str(b).isdigit():
                        num2.append(b)

            if len(num1) == len(num2) and puzzle_e != puzzle_s:
                wrong_msg = number_font.render("You have enterd some incorrect numbers.",True,black)
                screen.blit(wrong_msg,[10,10])
                    

            #check for correctly completed puzzle
            if puzzle_e == puzzle_s:
                start = 2
        #victory screen after completed puzzle    
        elif start == 2:
            screen.fill(white)
            victory = title_font.render("YOU WIN!!",True,black)
            screen.blit(victory,[250,250])
            
            if (diff+str(puzzle_num)) not in completed:
                completed.append((diff+str(puzzle_num)))
                info = open(filename,"w")
                print completed
                for q in completed:
                    new_info = info.write(q+"\n")
                info.close()
                
            back = number_font.render("BACK",True,black)
            screen.blit(back,[10,550])
            if (pos_x > 10 and pos_x < 105 ) and (pos_y > 550 and pos_y < 580 ):
                  back = number_font.render("BACK",True,red)
                  screen.blit(back,[10,550])
                  if event.type == pygame.MOUSEBUTTONDOWN:
                        start = 0
                        diff = ""
                        new = True
                        puzzle_num = random.choice([1,2,3])
                        count = 0
                        
    
    pygame.display.update()
    
