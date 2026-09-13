finput = input("camelCase: ")

print("snake_case: ", end="")

for char in finput:
    if char.islower():
        print(char, end="")

    else:
        print(f"_{char.lower()}", end="")

print("")
