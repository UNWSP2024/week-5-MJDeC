# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.
def math():
  print(""" 247
+129""")
  answer=int(input("What is the answer to the math problem?"))
  if answer==376:
    print('Yay! You can do addition! I hope you did not have to use your fingers...')
  else:
    print('What a loser... The answer is 376.')

math()      
