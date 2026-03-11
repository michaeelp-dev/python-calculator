import operations

def askInput():
    try:
        return float(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return askInput()

newNumber = askInput()

while True:
    operation = input("Enter operation (+ - * /), 'exit' or 'clear': ")

    if operation == "exit":
        print("Exiting calculator.")
        break

    elif operation == "clear":
        newNumber = askInput()
        print("Calculator reset.")

    elif operation in ['+', '-', '*', '/']:
        try:
            nextNumber = float(input("Enter another number: "))

            if operation == '+':
                newNumber = operations.add(newNumber, nextNumber)

            elif operation == '-':
                newNumber = operations.subtract(newNumber, nextNumber)

            elif operation == '*':
                newNumber = operations.multiply(newNumber, nextNumber)

            elif operation == '/':
                newNumber = operations.divide(newNumber, nextNumber)

            print("Result:", newNumber)

        except ValueError:
            print("Invalid number.")

        except ZeroDivisionError:
            print("Cannot divide by zero.")

    else:
        print("Invalid operation.")