import random

def intro():
        print("Welcome to Rock, Paper, Scissors!\nYou will play against the computer.")
        print("Here is how it works:")
        print("Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.\n")
        print("The game will keep track of your wins, losses, and ties.")
        print("Let's see how many rounds you can win against the computer!\n")
        print("Press Q or q to quit the game at any time.\n")

def gametime ():
        print("Let's start the game!")
        print("You can choose from the following options:")
        print("1. Rock - Type R or r.")
        print("2. Paper - Type P or p.")
        print("3. Scissors - Type S or s.\n")
        print("Type X to see current game statistics.\n")

userwins = 0
userlosses = 0
userties = 0

computerwins = 0
computerlosses = 0
computerties = 0

intro()
gametime()
possblechoices = ["rock", "paper", "scissors"]
computer_choice = random.choice(possblechoices)
inputuserchoice = input("Please enter your choice: ").strip().lower()
while inputuserchoice != 'q' or inputuserchoice != 'Q':
        if inputuserchoice in ['r', 'p', 's', 'R', 'P', 'S']:
                user_choice = {'r': 'rock', 'p': 'paper', 's': 'scissors'}[inputuserchoice]
                print(f"You chose {user_choice}.")
                print(f"The computer chose {computer_choice}.")
                
                if user_choice == computer_choice:
                        print("It's a tie!\n")
                        userties += 1
                        computerties += 1
                elif (user_choice == "rock" and computer_choice == "scissors") or \
                         (user_choice == "paper" and computer_choice == "rock") or \
                         (user_choice == "scissors" and computer_choice == "paper"):
                        print("You win!\n")
                        userwins += 1
                        computerlosses += 1
                else:
                        print("You lose!\n")
                        userlosses += 1
                        computerwins += 1
        elif inputuserchoice in ['x', 'X']:
                print("Current game statistics:")
                print(f"Your stats: {userwins} wins, {userlosses} losses, {userties} ties.")
                print(f"Computer stats: {computerwins} wins, {computerlosses} losses, {computerties} ties.\n")
        else:
                print("Invalid choice. Please choose R, P, S, or Q to quit.\n")
        
        computer_choice = random.choice(possblechoices)
        inputuserchoice = input("Please enter your choice: ").strip().lower()

print("Thanks for playing!")
print(f"Your stats: {userwins} wins, {userlosses} losses, {userties} ties.")
print(f"Computer stats: {computerwins} wins, {computerlosses} losses, {computerties} ties.")
