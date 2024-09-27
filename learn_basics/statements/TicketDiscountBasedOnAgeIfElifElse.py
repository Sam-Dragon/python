age = int(input("Enter your age\n"))

# Nested If-elif-else stmt
if 5 <= age <= 12:
    print("Please pay $7")
elif 12 < age <= 60:
    print("Please pay $12")
else:
    print("Please pay $10")
