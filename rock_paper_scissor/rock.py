import random
user_input = input("Please select your choice: rock, paper or scissor?")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print("You chose {} and computer chose {}.\n".format(user_input, computer_action))

if user_input == computer_action:
    print("Same choices!! It's a tie")
elif user_input == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_input == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_input == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
