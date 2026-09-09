user_input = input("Greeting: ")
input_format = user_input.casefold().strip()

if input_format.startswith("hello"):
    print("$0")

elif input_format.startswith("h"):
    print("$20")

else:
    print("$100")
