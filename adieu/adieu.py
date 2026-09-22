import inflect
p = inflect.engine()

names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break

o = p.join(names)
print(f"\nAdieu, adieu, to {o}")
