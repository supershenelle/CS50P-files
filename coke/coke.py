due = 50

while True:
    print(f"Amount Due: {due}")
    coin = int(input("Insert Coin: "))

    if coin in {5, 10, 25}:
        due = due - coin

    if due <= 0:
        break

print(f"Change Owed: {abs(due)}")
