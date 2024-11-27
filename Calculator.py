# Function for addition
def add(x, y):
    return x + y

# Function for subtraction
def subtract(x, y):
    return x - y

# Function for multiplication
def multiply(x, y):
    return x * y

# Function for division
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Displaying the options
def show_menu():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

# Main function to run the calculator
def calculator():
    while True:
        show_menu()

        # Take input from the user
        choice = input("Enter choice (1/2/3/4 or 'C' to Cancel): ")

        # If user chooses 'q', exit the program
        if choice == 'C':
            print("Exiting the calculator. Goodbye!")
            break

        # Check if the input is a valid operation
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        else:
            print("Invalid input. Please choose a valid operation (1/2/3/4).")

# Running the calculator function
calculator()