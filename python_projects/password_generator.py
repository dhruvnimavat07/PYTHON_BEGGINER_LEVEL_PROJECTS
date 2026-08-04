import random


def password_generator():
    """
    Generate 4 password suggestions.

    The user enters a username.
    The program creates 4 passwords.
    The user can select one password.

    Returns:
        None
    """

    symbols = ["@", "#", "$", "&", "*", "!"]

    print("===== PASSWORD GENERATOR =====")

    user_name = input("Enter Your User Name: ")

    password1 = user_name + str(random.randint(100, 999)) + random.choice(symbols)

    password2 = random.choice(symbols) + user_name + str(random.randint(1000, 9999))

    password3 = (
        user_name.capitalize() + random.choice(symbols) + str(random.randint(10, 99))
    )

    password4 = str(random.randint(100, 999)) + user_name + random.choice(symbols)

    print("\n===== PASSWORD SUGGESTIONS =====")
    print("1.", password1)
    print("2.", password2)
    print("3.", password3)
    print("4.", password4)

    choice = input("\nSelect Password (1-4): ")

    if choice == "1":
        print("\nSelected Password:", password1)

    elif choice == "2":
        print("\nSelected Password:", password2)

    elif choice == "3":
        print("\nSelected Password:", password3)

    elif choice == "4":
        print("\nSelected Password:", password4)

    else:
        print("\nInvalid Choice")


password_generator()
