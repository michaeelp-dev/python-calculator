import operations

numberA = float(input("Enter the first number: "))
numberB = float(input("Enter the second number: "))


operation = input("Enter the operation: ")

match operation:
    case "+":
        result = operations.add(numberA, numberB)
    case "-":
        result = operations.subtract(numberA, numberB)
    case "*":
        result = operations.multiply(numberA, numberB)
    case "/":
        result = operations.divide(numberA, numberB)
    case "**":
        result = operations.power(numberA, numberB)
print(f"The result is: {result}")