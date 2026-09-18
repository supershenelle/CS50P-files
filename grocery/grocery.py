grocery = {}

while True:
    try:
        for i in range(100):
            item = input("").casefold()
            grocery[item] = grocery.get(item, 0) + 1

    except EOFError:
        print("")
        for item in sorted(grocery):
            print(grocery[item], item.upper())

        break
