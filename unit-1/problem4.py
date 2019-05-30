# Functions to add, subtract, multiply and divide
def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

user_input = input('What calculation would you like to do? (add, sub, mult, div)\n')

num1 = int(input('What is number 1? '))
num2 = int(input('What is number 2? '))

if user_input == "add":
    print(num1, "+", num2, "=", add(num1,num2))
elif user_input == "sub":
    print(num1, "-", num2, "=", subtract(num1,num2))
elif user_input == "mult":
    print(num1, "*", num2, "=", multiply(num1,num2))
elif user_input == "div":
    print(num1, "/", num2, "=", divide(num1,num2))
else:
    print('Invalid input')