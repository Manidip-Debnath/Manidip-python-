def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

print("Welcome to the BMI Calculator!")
while True:
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        continue
    
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)
    
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")
    
    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != 'yes':
        break

print("Thank you for using the BMI Calculator!")
