user_name = input("Enter the name?\n")
print("Entered name :: " + user_name + "\n")

pet_name = input("Enter the pet name?\n")
print("Entered pet name :: " + pet_name + "\n")

temp = user_name
user_name = pet_name
pet_name = temp

print("user name :: " + user_name + ", pet name :: " + pet_name)
