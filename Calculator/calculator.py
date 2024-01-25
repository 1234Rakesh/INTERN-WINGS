#TASK -1  `CALCULATER`
# To create a straightforward calculator with fundamental arithmetic 
# functions, request user input for two numbers and their 
# chosen mathematical operation. Execute the computation and 
# present the outcome.

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
    
def Modulo(x, y):
    if y != 0:
        return x % y
    else:
        return "Error: Division by zero"
    
def calculator():
    while True:
            print("------------ Simple Calculator -----------------\n")
            print("   Choose operation:    ")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Modulo Division")
            print("6. Exist The calculator")
            

            operation = input("\nEnter choice (1/2/3/4/5/6): ")

            if operation not in ('1', '2', '3', '4','5','6'):
                print("\nInvalid choice. Please choose a valid operation.")

            if operation == '1':
                num1 = int(input("\n\nEnter first number: "))
                num2 = int(input("Enter second number: "))
                result = add(num1, num2)
                print(f"{num1} + {num2} = {result}")
                
            elif operation == '2':
                num1 = int(input("\nEnter first number: "))
                num2 = int(input("Enter second number: "))
                result = subtract(num1, num2)
                print(f"{num1} - {num2} = {result}")
                
            elif operation == '3':
                num1 = int(input("\nEnter first number: "))
                num2 = int(input("Enter second number: "))
                result = multiply(num1, num2)
                print(f"{num1} * {num2} = {result}")
                
            elif operation == '4':
                num1 = int(input("\nEnter first number: "))
                num2 = int(input("Enter second number: "))
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
                
            elif operation == '5':
                num1 = int(input("\nEnter first number: "))
                num2 = int(input("Enter second number: "))
                result = Modulo(num1, num2)
                print(f"{num1} % {num2} = {result}")
                
            elif operation == '6':
                print("\n 🙏 Thanks for Using This calculator 🙏 !")
                exit()
                
if __name__ == "__main__":
    calculator()

