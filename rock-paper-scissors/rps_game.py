import random

print("Welcome to Rock-Paper-Scissors game!")

valid_choices = ["rock", "paper", "scissors"]

your_choice = input("Enter your choice (rock, paper, scissors): ").lower()

if your_choice not in valid_choices:
    print("Invalid choice. Please choose rock, paper, or scissors, :(")

else:
    computer_choice = random.choice(valid_choices)
    print(f"computer choice was {computer_choice}")

    if your_choice == computer_choice:
        print(f"Both players selected {your_choice}. It's a tie!")
    else:
        if your_choice == "rock":
            if computer_choice == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif your_choice == "paper":
            if computer_choice == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif your_choice == "scissors":
            if computer_choice == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")
        