def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def calculator():
    print("Simple Calculator")
    print("Choose operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation = input("Enter choice (1/2/3/4): ")

    if operation not in ('1', '2', '3', '4'):
        print("Invalid choice. Please choose a valid operation.")
        return

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if operation == '1':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif operation == '2':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif operation == '3':
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif operation == '4':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")

if __name__ == "__main__":
    calculator()
