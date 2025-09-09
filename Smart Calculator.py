def smart_calculator():
    memory = None  # Start with empty memory
    print("Welcome to the Smart Calculator!")

    while True:
        print(f"\n-- Smart Calculator (Memory: {memory if memory is not None else '(empty)'}) --")

        # First number (or recall)
        first = input("Enter the first number (or 'r' to recall): ").strip()
        if first.lower() == "r":
            if memory is None:
                print("Error: Memory is empty.")
                continue
            first_num = memory
            print(f"Recalling {first_num} from memory.")
        else:
            try:
                first_num = float(first)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

        # Operator
        operator = input("Enter an operator (+, -, *, /, c to clear): ").strip()
        if operator == "c":
            if memory is None:
                print("Memory is already clear.")
            else:
                print(f"Value {memory} cleared from memory.")
                memory = None
            continue
        if operator not in ["+", "-", "*", "/"]:
            print("Invalid operator. Please try again.")
            continue

        # Second number
        second = input("Enter the second number: ").strip()
        try:
            second_num = float(second)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Perform calculation
        try:
            if operator == "+":
                result = first_num + second_num
            elif operator == "-":
                result = first_num - second_num
            elif operator == "*":
                result = first_num * second_num
            elif operator == "/":
                if second_num == 0:
                    raise ZeroDivisionError
                result = first_num / second_num

            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero. Please try again.")
            continue

        # Store in memory?
        store = input("Store result in memory? (y to store, any other key to continue): ").strip().lower()
        if store == "y":
            memory = result
            print(f"Value {memory} stored in memory.")

        # Continue?
        again = input("Do you want to perform another calculation? (type 'no' or 'n' to quit): ").strip().lower()
        if again in ["no", "n"]:
            print("Exiting Smart Calculator. Goodbye!")
            break


# Run the calculator
smart_calculator()
