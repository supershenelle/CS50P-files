import random as r

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except ValueError:
        continue

key = r.randint(1, n)
while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess > key:
                print("Too large!")

            elif guess < key:
                print("Too small!")

            else:
                print("Just right!")
                break
    except ValueError:
        continue

