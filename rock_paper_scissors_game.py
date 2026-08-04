import random

print("===== ROCK PAPER SCISSORS =====")

print("1. User VS Computer")
print("2. Player 1 VS Player 2")

option = input("Enter Your Choice (1 or 2): ")

# ---------------- USER VS COMPUTER ----------------

if option == "1":

    name = input("Enter Your Name: ")

    choices = ["rock", "paper", "scissors"]

    user = input("Enter rock, paper or scissors: ").lower()

    computer = random.choice(choices)

    print("Computer Selected:", computer)

    if user == computer:
        print("MATCH DRAW 🎰")

    elif user == "rock" and computer == "scissors":
        print("Congratulations", name, "Wins 🎊")

    elif user == "paper" and computer == "rock":
        print("Congratulations", name, "Wins 🎊")

    elif user == "scissors" and computer == "paper":
        print("Congratulations", name, "Wins 🎊")

    else:
        print("🎊 Computer Wins 🎊")


# ---------------- PLAYER VS PLAYER ----------------

elif option == "2":

    player1 = input("Enter Player 1 Name: ")
    player2 = input("Enter Player 2 Name: ")

    choice1 = input(player1 + ", Enter rock, paper or scissors: ").lower()

    print("\n" * 20)

    choice2 = input(player2 + ", Enter rock, paper or scissors: ").lower()

    if choice1 == choice2:
        print("Match Draw 🎰")

    elif choice1 == "rock" and choice2 == "scissors":
        print("Congratulations", player1, "Wins 🎊")

    elif choice1 == "paper" and choice2 == "rock":
        print("Congratulations", player1, "Wins 🎊")

    elif choice1 == "scissors" and choice2 == "paper":
        print("Congratulations", player1, "Wins 🎊")

    else:
        print("Congratulations", player2, "Wins 🎊")

else:
    print("Invalid Choice ⚠️ ")
