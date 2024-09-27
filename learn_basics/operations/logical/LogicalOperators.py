number = int(input("Enter the number?"))

if not number:
    print("Not a number")
if number >= 5 and number <= 18:
    print("Person is Minor")
if number > 18 and number <= 60:
    print("Person is Major")
if number > 60 or (number > 60 and number < 100):
    print("Person is senior")
