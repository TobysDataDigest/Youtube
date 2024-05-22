def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."


def calculator():
    print("Welcome to the Calculator!")

    while True:
        print("\nPlease select operation, or type 'quit' to exit:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Enter choice (1/2/3/4) or 'quit': ").lower()

        if choice == 'quit':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                first_num = float(input("Please enter the first number: "))
                second_num = float(input("Please enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == "1":
                print("Result:", add(first_num, second_num))
            elif choice == "2":
                print("Result:", subtract(first_num, second_num))
            elif choice == "3":
                print("Result:", multiply(first_num, second_num))
            elif choice == "4":
                print("Result:", divide(first_num, second_num))
        else:
            print("Invalid choice. Please try again.")


calculator()
