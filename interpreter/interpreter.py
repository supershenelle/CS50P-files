expres = input("Expression: ")
parts = expres.split()

num1 = float(parts[0])
op = parts[1]
num2 = float(parts[2])

match op:
    case "+":
        print(num1 + num2)

    case "-":
        print(num1 - num2)

    case "*":
        print(num1 * num2)

    case "/":
        print(num1 / num2)
