# Name: Ben Koczwara
# Date: Sept.13,2013
# Purpose: to create a quiz of 10 questions that are true or false answers

print "True/False Football Quiz"
print "------------------------"
print
print "This program asks you 10 True or False questions about football"
print
again = "y"
while again == "y":
      questions = ["'Mean' Joe Greene played linebacker.",
            "The first Super Bowl was held in Los Angeles.",
            "A touchdown is worth 7 points.",
            "Barry Sanders' nickname was 'Sweetness'.",
            "Deion Sander wore 21 with every team he played for.",
            "Dan Marino never won a super bowl.",
            "Joe Nameth guaranteed super bowl 3 victory.",
            "The record for the longest field goal is 60 yards.",
            "The CFL field is larger than the NFL field.",
            "The Buffalo Bills lost 4 super bowls in a row"]
      answers = ["F","T","F","F","F","T","T","F","T","T"]
      users_answers = []

      
      for x in range (0,10):
            right = False
            while not right:
                  print str(x+1)+".",questions[x],
                  answer = raw_input("(T)rue or (F)alse: ").upper()
                  if len(answer) > 1 or answer not in ["F","T"] or len(answer) == 0:
                        print "You can only enter 'T' or 'F'"
                  else:
                        right = True
            users_answers.append(answer)
            
      print
      print "Results"
      print "-------"
      print
      correct = 0

      for x in range(0,10):
            print questions[x]
            print "Your answer:",users_answers[x],"Correct answers:",answers[x]
            if users_answers[x] == answers[x]:
                  correct += 1

      print "You got",correct,"out of 10 correct."
      print


      again = "D"
            
            
            
            
