import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("Password Generator")
    try:
        length = int(input("Enter the preferred password length: "))
        if length <= 0:
            print("Please enter a valid positive length.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    password = generate_password(length)
    print(f"Generated Password: {password}")
    print(int(password))

if __name__ == "__main__":
    password_generator()
