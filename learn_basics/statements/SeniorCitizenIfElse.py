name = input("Enter your name\n")
age = int(input("Enter your age\n"))

if age > 60:
    print(f"{name} is senior citizen. Give 15% discount")
else:
    print(f"{name} is normal. No discounts")
