import random

random_number = random.randint(1, 13)
user_guess = input("enter your guess=")
if user_guess == "above" and random_number > 7:
    print("you win")
elif user_guess == "below" and random_number < 7:
    print("you won")
elif user_guess == "equal" and random_number == 7:
    print("you won")
else:
    print("you lost")
