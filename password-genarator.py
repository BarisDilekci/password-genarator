import random
import string


def generate_password(nr_letters, nr_symbols, nr_numbers):
    """
    Generate a password with the specified number of letters, symbols, and numbers.

    Parameters:
        nr_letters (int): Number of letters in the password.
        nr_symbols (int): Number of symbols in the password.
        nr_numbers (int): Number of numbers in the password.

    Returns:
        str: Generated password.
    """
    letters = string.ascii_letters
    symbols = "!#$%&'()*+"
    numbers = string.digits

    # Generate random characters for each category
    password_list = [
                        random.choice(letters) for _ in range(nr_letters)
                    ] + [
                        random.choice(symbols) for _ in range(nr_symbols)
                    ] + [
                        random.choice(numbers) for _ in range(nr_numbers)
                    ]

    # Shuffle the password list to ensure randomness
    random.shuffle(password_list)

    # Join the list into a string to form the password
    return ''.join(password_list)


def get_input(prompt, type_cast=int):
    """
    Get user input and ensure it is a valid integer.

    Parameters:
        prompt (str): The prompt message to display to the user.
        type_cast (callable): Function to cast the input to the desired type (default is int).

    Returns:
        int: Validated user input.
    """
    while True:
        try:
            value = type_cast(input(prompt))
            if value < 0:
                raise ValueError("The number must be positive.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")


def main():
    print("Welcome to the PyPassword Generator!")

    nr_letters = get_input("How many letters would you like in your password?\n")
    nr_symbols = get_input("How many symbols would you like?\n")
    nr_numbers = get_input("How many numbers would you like?\n")

    password = generate_password(nr_letters, nr_symbols, nr_numbers)

    print(f"Your password: {password}")


if __name__ == "__main__":
    main()
