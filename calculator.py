def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    if n2 == 0:
        raise ValueError("Cannot divide by zero")
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def get_number(prompt):
    """Get a valid float input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number")

def calculate():
    """Run the calculator with chained calculations."""
    run_program = "y"
    while run_program.lower() == "y":
        num1 = get_number("Enter the first number: ")
        chain_calculation = "y"
        
        while chain_calculation.lower() == "y":
            # Display operators
            print("Available operators:", ", ".join(operations.keys()))
            
            operator = input("Enter the operator: ")
            num2 = get_number("Enter the second number: ")
            
            # Direct dictionary lookup
            operation = operations.get(operator)
            if operation:
                try:
                    result = operation(num1, num2)
                    print(f"{num1} {operator} {num2} = {result}")
                    num1 = result  # Chain the result for the next calculation
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print(f"Invalid operator. Please use one of: {', '.join(operations.keys())}")
            
            # Ask to continue with the current result
            chain_calculation = input("Do you want to continue from here (y/n): ").strip() or "n"
        
        # Ask to start a new calculation
        run_program = input("Do you want to continue calculating (y/n): ").strip() or "n"

if __name__ == "__main__":
    try:
        calculate()
    except KeyboardInterrupt:
        print("\nCalculator stopped.")