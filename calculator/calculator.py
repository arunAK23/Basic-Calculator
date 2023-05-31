def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("Welcome to the Basic Calculator!")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1-4): ")

if choice == '1':
    result = add(num1, num2)
    print("The result is:", result)
elif choice == '2':
    result = subtract(num1, num2)
    print("The result is:", result)
elif choice == '3':
    result = multiply(num1, num2)
    print("The result is:", result)
elif choice == '4':
    result = divide(num1, num2)
    print("The result is:", result)
else:
    print("Invalid choice. Please select a number from 1 to 4.")
