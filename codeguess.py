import random

def get_guess():
  return list(input("What is your guess?"))

def generate_code():
  numbers = [str(num) for num in range(10)]

  random.shuffle(numbers)
  return numbers[:3]

def genereate_clue(code, user_guess):
  if user_guess == code:
    return "You got it!"

  clues = []

  for ind, num in enumerate(user_guess):
    if num == code[ind]:
      clues.append("match")
    elif num in code:
      clues.append("Correct number, wrong position")

  if clues == []:
    return ["Nope"]
  else:
    return clues

print("Welcome to the Code Breaker!")

secret_code = generate_code()

clue_report = []

while clue_report != "You got it!":
  guess = get_guess()

  clue_report = genereate_clue(guess, secret_code)
  print("result of your guess")
  for clue in clue_report:
    print(clue)