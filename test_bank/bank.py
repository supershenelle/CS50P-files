def main():
    user_input = input("Greeting: ")
    input_format = user_input.casefold().strip()
    money = value(input_format)
    print(f"${money}")

def value(greeting):
    if greeting.startswith("hello"):
        return 0

    elif greeting.startswith("h"):
        return 20

    else:
        return 100


if __name__ == "__main__":
    main()
