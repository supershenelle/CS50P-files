menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = float(0)
    while True:
        try:
            _input = input("Item: ")
            _input = _input.title()
            total = total + menu[_input]
            print(f"Total: ${total:.2f}")

        except KeyError:
            continue

        except EOFError:
            print("")
            break

if __name__ == "__main__":
    main()
