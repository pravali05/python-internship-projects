
def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input! Enter a number.")


def calculator():
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Choose operation: ")

    if choice == "1":
        print("Result:", a + b)
    elif choice == "2":
        print("Result:", a - b)
    elif choice == "3":
        print("Result:", a * b)
    elif choice == "4":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid choice")


def converter():
    print("1. KM to Miles")
    print("2. Celsius to Fahrenheit")

    choice = input("Choose conversion: ")

    if choice == "1":
        km = get_number("Enter kilometres: ")
        print("Miles:", km * 0.621371)

    elif choice == "2":
        c = get_number("Enter Celsius: ")
        print("Fahrenheit:", c * 9/5 + 32)

    else:
        print("Invalid choice")


while True:
    print("\n--- MAIN MENU ---")
    print("1. Calculator")
    print("2. Unit Converter")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        calculator()
    elif choice == "2":
        converter()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")
    