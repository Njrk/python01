#!/usr/bin/python3

print("Welcome to the Calculator Program!\n")

while True:
    try:
        first_number = float(input("Please enter the first number: "))
        break
    except ValueError:
        print("Incorrect data has been entered. Please enter a number.")

while True:
    try:
        second_number = float(input("Please enter the second number: "))
        break
    except ValueError:
        print("Incorrect data has been entered. Please enter a number.")

operation = int(input('''
Please select an operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
        
Enter your choice (1-4): '''))

while True:
    if 0 < operation < 5:
        break
    else:
        operation = int(input("Please select an existing operation (1-4): "))

if operation == 1:
    result = first_number + second_number
    operation_name = "addition"
elif operation == 2:
    result = first_number - second_number
    operation_name = "subtraction"
elif operation == 3:
    result = first_number * second_number
    operation_name = "multiplication"
else:
    result = first_number / second_number if second_number > 0 else "division by zero in not allowed"
    operation_name = "division"

if not isinstance(result, str):
    result = int(result) if result.is_integer() else result

print("\nThe result of", operation_name, "is: ", result)
