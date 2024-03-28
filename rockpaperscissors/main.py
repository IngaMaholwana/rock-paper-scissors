import random

options = ["Rock", "Paper", "Scissors"]

player = input("Choose Rock, Paper, or Scissors: ").capitalize()

computer_choice = random.choice(options)

print("You chose:", player)
print("Computer chose:", computer_choice)
 
if player == computer_choice:
    print("It's a tie!")
elif player == 'Rock':
    if computer_choice == 'Paper':
        print("Computer wins!")
    else:
        print("You win!")
elif player == 'Paper':
    if computer_choice == 'Scissors':
        print("Computer wins!")
    else:
        print("You win!")
elif player == 'Scissors':
    if computer_choice == 'Rock':
        print("Computer wins!")
    else:
        print("You win!")
else:
    print("Please enter 'Rock', 'Paper', or 'Scissors'.")
