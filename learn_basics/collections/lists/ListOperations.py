employees = []
print(f"Employees :: {employees}")

print("\n>> Append [Add]")

employees.append("Ram")
employees.append("Shyam")
print(f"Employees :: {employees}")

print("\n>> Remove [Delete]")

employees.remove("Ram")
print(f"Employees :: {employees}")

print("\n>> extend [Add Lists to End]")

employees.extend(["Jam", "Kim"])
print(f"Employees :: {employees}")

print("\n>> index")
print(f"Employees[0] :: {employees[0]}")

print("\n>> Length")
print(f"Employees Length :: {len(employees)}")

