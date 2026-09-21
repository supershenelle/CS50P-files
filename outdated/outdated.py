date = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        dateint = input("Date: ")

        if "/" in dateint:
            month, day, year = map(int, dateint.split("/"))

        elif "," in dateint:
            month, dayyear = dateint.split(" ", maxsplit = 1)
            day, year = map(int, dayyear.split(", "))

            month = date.index(month)
            month = int(month)+1

        else:
            day, month, year = dateint.split(" ")
            month = date.index(month)
            month = int(month)+1
            day = int(day)
            year = int(year)

        if not (1 <= month <= 12) or not (1<= day <= 31):
            raise ValueError()

        print(f"{year}-{month:02}-{day:02}")
        break

    except ValueError:
        continue
