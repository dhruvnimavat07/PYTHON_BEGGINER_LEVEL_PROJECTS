import random


def number_guessing_game():
    """
    Start a simple number guessing game.

    The computer randomly selects a number between
    1 and 10. The player continues guessing until
    the correct answer is entered.
    """

    secret_number = random.randint(1, 100)
    attempt_count = user_attempts = 0
    print("WELCOME TO THE NUMBER GUESSING GAME 🎯")

    limit = 10
    while user_attempts <= 10:

        guess = int(input("Guess Number (1-100): "))
        user_attempts += 1

        if guess == secret_number:
            print(
                f"🎉 CONGRATULATIONS 🎉\nYou guessed the number in {user_attempts} attempts.!"
            )
            break

        elif guess > secret_number:
            print("Your Guessing is Too high ⚠️", "\n")

        elif guess < secret_number:
            print("Your Guessing is Too Low ⚠️", "\n")

        if limit == 0:
            print("YOU ARE DISCOLIFIED ❌")
            break
        else:
            limit -= 1
            print(f"attemps left {limit}")


number_guessing_game()
