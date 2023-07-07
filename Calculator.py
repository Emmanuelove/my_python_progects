
# My first calculator



def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def exponent(n1, n2):
    return n1 ** n2


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": exponent
}

def calculator():
    num1 = float(input("What's the first number?: "))

    for symbols in operators:
        print(symbols)

    continue_calculation = True
    while continue_calculation:
        operators_symbol = input("Pick an operator: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operators[operators_symbol]
        print(operators[operators_symbol])
        answer = calculation_function(num1, num2)

        print(f"{num1} {operators_symbol} {num2} = {answer}")

        choice = ["y", "n"]
        while True:
            continu = input(f"Type 'y' to continue calculating with the previous result {answer}, or type 'n' to start a new calculation?\n").lower()
            if continu not in choice:
                print("Invalid answer")
                continue
            if continu == "y":
                num1 = answer
                break
            elif continu == "n":
                continue_calculation = False
                calculator()

calculator()  

    # operators_symbol = input("Pick another operators: ")
    # num3 = int(input("What's the next number?: "))
    # calculation_function = operators[operators_symbol]
    # second_answer = calculation_function(calculation_function(num1, num2), num3)

    # print(f"{first_answer} {operators_symbol} {num3} = {second_answer}")
  
    
