def add_numbers(a, b):
    return a + b

# Function to handle invalid inputs
def get_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

num1 = get_input("Enter first number: ")
num2 = get_input("Enter second number: ")

result = add_numbers(num1, num2)
print("The sum is:", result)
