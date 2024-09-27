first_number = input("Enter the first number  ?")
print(f"Entered first number :: {first_number}")

last_number = input("Enter the last number ?")
print(f"Entered last number :: {last_number}")

first_number = int(first_number)
last_number = int(last_number)

print()
first_number = first_number + last_number
print(f"Sum of the numbers :: {first_number}")

last_number = first_number - last_number
print(f"Subtract second number from sum :: {last_number}")

first_number = first_number - last_number
print(f"Subtract result from sum :: {first_number}")

print(f"First Number :: {first_number}, Last Number :: {last_number}")
