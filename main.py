import time

print("Welcome to Grade Generator")
print()
print("I will ask you a few questions to determine your letter grade and percentage score.")
print()


def endGame():
  while True:
    input()
    print()
    print("Thank you for using Grade Generator.")
    print()
    print("To generate another grade please click Stop on top right page and click Run")
    continue


def getStudentName():
  while True:
    studName = input("What is your name?: ")
    print()
    if studName.isnumeric() == True:
      print()
      print("Please enter a valid name not numbers.")
      print()
      continue
    else:
      return studName


def getTestName():
  while True:
    
    name = input("What is the name of the test?: ")
    print()
    if name.isnumeric() == True:
      print()
      print("Please enter a valid name not numbers.")
      print()
      continue
    else:
      return name


def getMaxScore():
  while True:
    try:
      max_score = float(input("What is the maximum score you could receive for this test?: "))
      print()
    except ValueError:
      print()
      print("I am expecting positive numbers.")
      print()
      continue
    if max_score <= 0:
      print()
      print("Maximum score cannot be zero or negative.")
      print()
      continue
    else:
      return max_score

def getScore(maxScore):
  while True:
    try:
      score = float(input("What is the score you received for this test?: "))
      print()
    except ValueError:
      print()
      print("I am expecting numbers.")
      print()
      continue
    if score < 0:
      print()
      print("If you got a negative mark it means you got 0.00 % and letter grade is U. Please try scores greater or equal to zero. ")
      print("To generate another grade for another test please click Stop on top right of the console and then click Run")
      print()
      continue
    elif score > maxScore:
      print()
      print("Your score cannot be greater than the maximum score.")
      print()
      continue  
    else:
      return score      


def grade(score, maxScore, studName, name):
  perc = (score/maxScore) * 100
  print('Calculating percentage score for',name,"test...")
  time.sleep(3)
  print()

  if perc >= 90 and perc <=100:
    print('Hello',studName,'you are a phenomenal student!')
    print()
    print("Letter Grade: A+  Percentage: {:0.2f} %".format(perc))
  if perc >= 80 and perc <=89:
    print('Hello',studName,' excellent student!')
    print()
    print("Letter Grade: A  Percentage: {:0.2f} %".format(perc))  
  if perc >= 70 and perc <=79:
    print('Hello',studName,'you are great student!')
    print()
    print("Letter Grade: B  Percentage: {:0.2f} %".format(perc))    
  if perc >= 60 and perc <=69:
    print('Hello',studName,'you are a good student!')
    print()
    print("Letter Grade: C  Percentage: {:0.2f} %".format(perc))
  if perc >= 50 and perc <=59:
    print('Hello',studName,'you are a decent student!')
    print()
    print("Letter Grade: D  Percentage: {:0.2f} %".format(perc))
  if perc < 50:
    print('Hello',studName,'Do not give up, keep studying and your marks will get better.')
    print()
    print("Letter Grade: U  Percentage: {:0.2f} %".format(perc))
    
if __name__ == "__main__":
  studName = getStudentName()
  name = getTestName()
  maxScore = getMaxScore()
  score = getScore(maxScore)
  grade(score, maxScore, studName, name)
  endGame()