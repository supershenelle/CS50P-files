import random


def main():
    level = get_level()
    correctcount = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        key = x + y
        wrongcount = 0

        while True:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer != key:
                    print("EEE")
                    wrongcount += 1
                    if wrongcount == 3:
                        print(f"{x} + {y} = {key}")
                        break
                else:
                    correctcount += 1
                    break

            except ValueError:
                print("EEE")
                wrongcount += 1
                if wrongcount == 3:
                    print(f"{x} + {y} = {key}")
                    break

    print(f"Score: {correctcount}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in range(1, 4):
                return n
        except ValueError:
            continue


def generate_integer(level):
    level = int(level)

    if level == 1:
        return random.randint(0, 9)

    elif level == 2:
        return random.randint(10, 99)

    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
