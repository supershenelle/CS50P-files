def main():
    ftime = input("What time is it? ")
    ftime = convert(ftime)

    if 7.0 <= ftime <= 8.0:
        print("breakfast time")

    elif 12.0 <= ftime <= 13.0:
        print("lunch time")

    else:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    minutes = minutes / 60
    return hours + minutes

if __name__ == "__main__":
    main()
