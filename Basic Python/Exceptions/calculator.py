
def ask_for_information(current_number):
    while True:
        print(f"\nCurrent number: {current_number}")
        print("Choose one of the following options:")
        print("1. Add")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Delete result")
        print("6. Exit")

        option = input("Select an option (1-6): ")

        if option not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid option. Please choose a number between 1 and 6.")
            continue

        second_number = None

        if option in ["1", "2", "3", "4"]:
            while True:
                try:
                    second_number = float(input("Enter another number: "))
                    break
                except ValueError as e:
                    print(f"Invalid input. You must enter a valid number. Details: {e}")

        return option, second_number


def calculate(current_number, option, second_number):
    try:
        if option == "1":
            return current_number + second_number
        elif option == "2":
            return current_number - second_number
        elif option == "3":
            return current_number * second_number
        elif option == "4":
            if second_number == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return current_number / second_number
        else:
            return current_number
    except ZeroDivisionError as e:
        print(f"Error [ZeroDivisionError]: {e}")
        return current_number


def main():
    while True:
        try:
            current_number = float(input("Enter a number: "))
            break
        except ValueError as e:
            print(f"Invalid number, please try again. Details: {e}")

    while True:
        try:
            option, second_number = ask_for_information(current_number)

            if option == "6":
                print("Goodbye!")
                break

            if option == "5":
                print("Result cleared. Enter a new number.")
                while True:
                    try:
                        current_number = float(input("Enter a new number: "))
                        break
                    except ValueError as e:
                        print(f"Invalid number, please try again. Details: {e}")
                continue

            current_number = calculate(current_number, option, second_number)

            if isinstance(current_number, float) and current_number.is_integer():
                print(f"Updated current number: {int(current_number)}")
            else:
                print(f"Updated current number: {current_number}")

        except Exception as error:
            print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()