user_choice = input("Rock, Paper, or Scissors? ")
# Rock0, Paper1, Scissors2
import random
options = [0,1,2]
computer_choice = random.choice(options)

if user_choice == "Rock":
    if computer_choice == 1:
        print("Rock vs Paper: You lose")
    elif computer_choice == 2:
        print("Rock vs Scissors: You win")
    else:
        print("Tie")
if user_choice == "Paper":
    if computer_choice == 0:
        print("Papaer vs Rock: You win")
    elif computer_choice == 2:
        print("Paper vs Scissors: You lose")
    else:
        print("Tie")
if user_choice == "Scissors":
    if computer_choice == 1:
        print("Scissors vs Paper: You win")
    elif computer_choice == 0:
        print("Scissors vs Rock: You lose")
    else:
        print("Tie")
