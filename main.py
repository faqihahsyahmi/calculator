import art

def add(n1, n2):
    return n1 + n2

#create function for subtract, multiply and divide
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide (n1, n2):
    return n1 / n2

#add these functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operation = { #STORING the func, NOT USING
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(art.logo)
    cont = True
    num1 = float(input("Key in first number: "))
    while cont:
        for op_symbol in operation:
            print(op_symbol)
        op = input("Pick an operation: ")
        num2 = float(input("Key in next number: "))

        output = operation[op](num1, num2)

        print(f"{num1} {op} {num2} = {output}")

        cont_calculate = input("Type 'y' to continue calculating with, or type 'n' to start a new calculation: ").lower()

        if cont_calculate == 'y':
            num1 = output
        else:
            cont = False
            print("\n"*100)
            #recursion - a func that is called inside itself...
            calculator()

calculator()