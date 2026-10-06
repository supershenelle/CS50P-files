def main():
    while True:
        try:
            percentage = convert(input("Fraction: "))
        except ValueError:
            print("Value Error")
        except ZeroDivisionError:
            print("Cannot divide by 0")
        else:
            break

    print(gauge(percentage))


def convert(fraction):
    xs, ys = fraction.split("/")
    x = int(xs)
    y = int(ys)

    if y == 0:
        raise ZeroDivisionError
    if x < 0 or y < 0 or x > y:
        raise ValueError

    return round(x / y * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
