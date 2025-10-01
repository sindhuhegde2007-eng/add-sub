# Function to perform addition and subtraction
def add_subtract(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else "Undefined (division by zero)"
    return addition, subtraction, multiplication, division



# Input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform operations
add, sub, mul, div = calculate_all(num1, num2)

# Display results
print(f"Addition: {num1} + {num2} = {sum_result}")
print(f"Subtraction: {num1} - {num2} = {diff_result}")
print(f"Multiplication: {num1} * {num2} = {mul}")
print(f"Division: {num1} / {num2} = {div}")






