# convert strint to input

number = input("Enter the number?")
print(type(number))

value = 0
try:
    value = int(number)
except Exception as e:
    print(f"Reset to default. Error :: {str(e)}")

print("Input = " + value)
