def check_temperature_fahrenheit(temp_f):  # Function definition header with one parameter
    if temp_f >= 86:  # 86°F ≈ 30°C
        print("It's a hot day!")  # Print statement
    elif temp_f >= 59:  # 59°F ≈ 15°C
        print("The weather is nice and mild.")  # Print statement
    else:
        print("It's cold outside, dress warmly!")  # Print statement

# Get temperature from the user and call the function
user_temp_f = float(input("Enter the temperature in Fahrenheit:\n"))  # Argument
check_temperature_fahrenheit(user_temp_f)  # Function call
