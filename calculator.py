import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def exponentiate(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def log(x, base):
    if base == 'e':
        return math.log(x)
    return math.log(x, base)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponentiate")
print("6. Square Root")
print("7. Logarithm")
print("8. Sine")
print("9. Cosine")
print("10. Tangent")

while True:
    choice = input("Enter choice(1-10): ")

    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):
        if choice == '6':
            num = float(input("Enter number: "))
            print("√", num, "=", sqrt(num))
        elif choice == '7':
            num = float(input("Enter number: "))
            base = input("Enter base (e for natural log): ")
            print("log", num, "base", base, "=", log(num, base))
        elif choice in ('8', '9', '10'):
            angle = float(input("Enter angle in degrees: "))
            if choice == '8':
                print("sin(", angle, ") =", sin(angle))
            elif choice == '9':
                print("cos(", angle, ") =", cos(angle))
            elif choice == '10':
                print("tan(", angle, ") =", tan(angle))
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))

            elif choice == '5':
                print(num1, "^", num2, "=", exponentiate(num1, num2))

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
    else:
        print("Invalid Input")
