def main():
    iinput = input("Input: ")
    shorten(iinput)

def shorten(word):
    for char in iinput:
    if char.casefold() in ["a", "e", "i", "o", "u"]:
        print("", end="")

    else:
        print(f"{char}", end="")

    print("")


if __name__ == "__main__":
    main()
