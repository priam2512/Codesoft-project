# for stone, paper, scissors
# 1 for stone
# -1 for paper
# 0 for scissors

computer = -1  # You can change this to a random selection later if needed
youstr = input("Enter your choice (s for Stone, p for Paper, c for Scissors): ")

# Mapping user input to values
youDict = {"s": 1, "p": -1, "c": 0}
reverseDict = {1: "Stone", -1: "Paper", 0: "Scissors"}

# Get the user's choice
you = youDict[youstr]

# Print choices
print(f"You chose {reverseDict[you]}")
print(f"Computer chose {reverseDict[computer]}")

# Decide the winner based on the conditions
if computer == you:
    print("It's a draw!")
else:
    if computer == -1 and you == 1:  # Paper vs Stone
        print("You win!")
    elif computer == -1 and you == 0:  # Paper vs Scissors
        print("You lose!")
    elif computer == 1 and you == -1:  # Stone vs Paper
        print("You lose!")
    elif computer == 1 and you == 0:  # Stone vs Scissors
        print("You win!")
    elif computer == 0 and you == -1:  # Scissors vs Paper
        print("You win!")
    elif computer == 0 and you == 1:  # Scissors vs Stone
        print("You lose!")
    else:
        print("Something went wrong!")