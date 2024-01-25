#TASK -2  `PASSWORD GENERATOR`
import string 
import random 

char = list(string.ascii_letters + string.digits + "!@#$^&*")
def generate_pass():
    password_len = int(input("How long would you like your password to be? "))

    random.shuffle(char)
    password =[]
    
    for x in range(password_len + 1):
        password.append(random.choice(char))
        
    random.shuffle(password)
    
    password = "".join(password)
    
    print("Your Password = ",password)
    
option = input("Do you want to generate a password? (Yes/No): ")
if option == 'Yes':
   generate_pass()
elif option == 'No':
    print("Bye!") 
    exit()
else:
    print("Invelaide Inpit ")
    exit()