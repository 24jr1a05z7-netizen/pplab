feet = float(input("Enter length in feet: "))

units = ["Inches","Yards","Miles","Millimeters","Centimeters","Meters","Kilometers"]
values = [feet*12, feet/3, feet/5280, feet*304.8, feet*30.48, feet*0.3048, feet*0.0003048]

print("Conversions:")
for i in range(len(units)):
    print(units[i], "=", values[i])
