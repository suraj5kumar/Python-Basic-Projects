"""
Making a rock paper scissor game
"""


def rockPaperScissor():
    import random

    # importing random module to select an option randomly by computer from choices

    options = ["rock", "paper", "scissors"]

    computer_choice = random.choice(options)
    user_choice = input("Enter your choice = ").lower()

    if user_choice in options:
        if (
            user_choice != "rock"
            and user_choice != "paper"
            and user_choice != "scissors"
        ):
            print("Invalid choice")
        elif (
            (user_choice == "rock" and computer_choice == "scissors")
            or (user_choice == "paper" and computer_choice == "rock")
            or (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("You won")
        elif user_choice == computer_choice:
            print("You tied")
        else:
            print(f"You lost, the computer choice was {computer_choice}")
    else:
        print("You have entered wrong choice.")


rockPaperScissor()
