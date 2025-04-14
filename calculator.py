def add(n1,n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,

}

keep_going = "y"
keep = "y"
while keep_going.lower() == "y":
    num1 = float(input("Enter the first number: "))
    while keep.lower() == "y":
        for symbol in operations:
            print(symbol)
        operator = input("Enter the operator: ")
        num2 = float(input("Enter the second number: "))
        found = False
        for key in operations:
            if key == operator:
                answer = operations[key] (num1,num2)
                print(f"{num1} {operator} {num2} = {answer}")
                found = True
                break
            

        if not found:
            print("Invalid operator")

        keep = str(input("Do you want to continue from here (y/N): "))
        if keep.lower() == "y":
            num1 = answer
    
    keep_going = str(input("Do you want to continue calculating (y\n): "))