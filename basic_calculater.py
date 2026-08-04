print("\033[1mHERE IS YOUR CALCULATER\033[0m")


def calculator(number1, number2, operator):
    """
    Perform a basic arithmetic operation.

    Parameters:
        number1 (float): First number.
        number2 (float): Second number.
        operator (str): +, -, *, /

    Returns:
        float or str:
            Result of calculation or error message.
    """

    if operator == "+" or operator == "1":
        return number1 + number2

    elif operator == "-" or operator == "2":
        return number1 - number2

    elif operator == "*" or operator == "3":
        return number1 * number2

    elif operator == "/" or operator == "4":
        if number2 == 0:
            return "Division by zero is not allowed."
        return number1 / number2

    else:
        return "Invalid Operator"


while True:
    first_number = float(input("Enter First Number :- "))
    second_number = float(input("Enter Second Number :-  "))
    operator = input(
        "[1].Addition(+)\n[2].Substraction(-)\n[3].Multiplication(*)\n[4].Division(/)\nWhich One Would You Like To Do :- "
    )

    result = calculator(first_number, second_number, operator)

    print("Result =", result)
    print()
