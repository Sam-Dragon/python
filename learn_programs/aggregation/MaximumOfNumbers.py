# Loop way
print("\nLoop way")
scores = [8, 65, 89, 86, 55, 91, 64, 89]
maximum = -1
for score in scores:
    if score > maximum:
        maximum = score

print(maximum)

# Direct Functions
print("\nInbuilt Function")
maximum = max(scores)
print(maximum)
