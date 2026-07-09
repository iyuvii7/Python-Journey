import random
print("Welcome to Rock, Paper, Scissors!")
list_of_choices = ["rock", "paper", "scissors"]
user_choice = input("Enter your choice (rock, paper, scissors):\n").lower()
computer_choice = random.choice(list_of_choices)
print(f"Computer chose: {computer_choice}")

if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if computer_choice == "paper":
        print("You lose! Paper beats Rock.")
    else:
        print("You win! Rock beats Scissors.")
elif user_choice == "paper":
    if computer_choice == "scissors":
        print("You lose! Scissors beats Paper.")
    else:
        print("You win! Paper beats Rock.")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print("You lose! Rock beats Scissors.")
    else:
        print("You win! Scissors beats Paper.")
else:
    print("Invalid choice. Please choose rock, paper, or scissors.")