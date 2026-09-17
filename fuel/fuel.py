def fuel(n):
    if not n > 1:
        print("E")
    elif n >= 99:
        print("F")
    else:
        print(f"{n}%")

def main():
    while True:
        try:
            frac = input("Fraction: ")
            xs, ys = frac.split("/")
            x = round(int(xs))
            y = round(int(ys))

            if x < 0 or y < 0 or (x/y) > 1:
                raise ValueError()
            if y == 0:
                raise ZeroDivisionError()

        except ValueError:
            print("Value Error")
        except ZeroDivisionError:
            print("Cannot divide by 0")
        else:
            break

    n = (x / y) * 100
    n = round(n)
    fuel(n)

if __name__ == "__main__":
    main()
