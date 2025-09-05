import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Rock crushes Scissors
# Scissors cut Paper
# Paper covers Rock

decision = int(input("What are you choosing? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
ok_decision = 0

if decision == 0 or decision == 1 or decision == 2:
    ok_decision = 1

while ok_decision == 0:
    if ok_decision == 0:
        decision = int(input("You should enter a valid number(0, 1, 2) to continue playing!\n"))
        if decision == 0 or decision == 1 or decision == 2:
            ok_decision = 1

if decision == 0:
    print(rock)
elif decision == 1:
    print(paper)
else:
    print(scissors)

computer_decisions = [rock, paper, scissors]

random_generate = random.randint(0, 2)
print("Computer chose: ")
print(computer_decisions[random_generate])

if decision == 0:
    if random_generate == 0:
        print("It is a draw result!\n")
    elif random_generate == 1:
        print("You lost! Computer won! Paper covers Rock!\n")
    else:
        print("You won! Computer lost! Rock crushes scissors!\n")

if decision == 1:
    if random_generate == 0:
        print("You won! Computer lost! Paper covers Rock!\n")
    elif random_generate == 1:
        print("It is a draw result!\n")
    else:
        print("You lost! Computer won! Scissors cut Paper!\n")

if decision == 2:
    if random_generate == 0:
        print("You lost! Computer won! Rock crushes Scissors!\n")
    elif random_generate == 1:
        print("You won! Computer lost! Scissors cut Paper\n")
    else:
        print("It is a draw result!\n")