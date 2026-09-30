def main():
    iinput = input("Input: ")
    print(shorten(iinput))

def shorten(word):
    result = ""
    for char in word:
        if char.casefold() not in ["a", "e", "i", "o", "u"]:
            result += char

    return result

if __name__ == "__main__":
    main()
