user_name = input("Enter the name?\n")
print("Entered name :: " + user_name + "\n")

pet_name = input("Enter the pet name?\n")
print("Entered pet name :: " + pet_name + "\n")

user_name = user_name + pet_name  # Rahul Sample
print(f"Concat the string :: {user_name}")

pet_name = user_name.replace(pet_name, "")
print(f"Subtract concat string with second string :: {pet_name}")

user_name = user_name.replace(pet_name, "")
print(f"Subtract concat string with previous string :: {user_name}")

print("user name :: " + user_name + ", pet name :: " + pet_name)
