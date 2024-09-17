#add
def add(n1, n2):
    return n1 + n2
#subtract
def subtract(n1, n2):
    return n1 - n2
#multiply
def multiply(n1, n2):
    return n1 * n2
#divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

for symbol in operations:
    print(symbol)
    

def calculator():
    from art import logo
    print(logo)
    num1 = float(input("What's the first number? "))
    calculation_finished = False
    while not calculation_finished:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        option = input(f"Type y to continue calculating with {answer}, or type n to start a new calculation: ")
        if option == "y":
            num1 = answer
        elif option == "n":
            calculator()
calculator()
