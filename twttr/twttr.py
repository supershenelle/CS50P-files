iinput = input("Input: ")

for char in iinput:
    if char.casefold() in ["a", "e", "i", "o", "u"]:
        print("", end="")

    else:
        print(f"{char}", end="")

print("")
