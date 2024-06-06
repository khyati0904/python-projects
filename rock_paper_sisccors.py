"""
Rock-Paper-Scissors Game

computer_choice= 

user_choice= Pick from rock,paper,scissor

if
elif
elif
...
...
else
"""
"""
import random

options=['rock','paper','scissors']

computer_choice = random.choice(options)
user_choice=input("Guess between rock,paper,scissor = ").lower()
"""

# ----IF-ELIF--ELSE

import random

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
user_choice = input("guess between rock,paper,scissors=").lower()
if user_choice == computer_choice:
    print("no one win")
elif user_choice == "rock" and computer_choice == "paper":
    print("computer_choice won")
elif user_choice == "paper" and computer_choice == "rock":
    print("user_choice won")
elif user_choice == "rock" and computer_choice == "scissors":
    print("computer_choice won")
elif user_choice == "scissors" and computer_choice == "rock":
    print("computer_choice won")
elif user_choice == "rock" and computer_choice == "scissors":
    print("computer_choice won")
elif user_choice == "scissors" and computer_choice == "rock":
    print("user_choice won")
else:
    print("you lost")

"""
if user_choice=="rock" and computer_choice=="scissors":
    print("You won")
elif user_choice=="paper" and computer_choice=="rock":
    print("You won")
elif user_choice=="scissors" and computer_choice=="paper":
    print("You won")
elif user_choice==computer_choice:
    print("You have tied")
else:
    print(f"You lost. Computer choose {computer_choice}")
"""
