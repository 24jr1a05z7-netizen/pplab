num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if abs(num1 - num2) <= 0.001:
    print("Close")
else:
    print("Not Close")
