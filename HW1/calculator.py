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
elif operation == 2:
    result = first_number - second_number
elif operation == 3:
    result = first_number * second_number
else:
    result = first_number / second_number if second_number > 0 else "division by zero in not allowed"

print("\nThe result of multiplication is: ", result)