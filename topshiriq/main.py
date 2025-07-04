import math_utils


num1 = float(input("Birinchi sonni kiriting: "))
num2 = float(input("Ikkinchi sonni kiriting: "))
operation = input("Amalni kiriting (+, -, *, /): ")
if operation == "+":
    result = math_utils.add(num1, num2)
elif operation == "-":
    result = math_utils.subtract(num1, num2)
elif operation == "*":
    result = math_utils.multiply(num1, num2)
elif operation == "/":
    result = math_utils.divide(num1, num2)
else:
    print("Noto'g'ri amal!")
    exit()

print(f"Natija: {result}")



