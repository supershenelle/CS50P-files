answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
answerf = answer.strip().casefold()

if answerf == "42" or answerf == "forty-two" or answerf == "forty two":
    print("Yes")

else:
    print("No")
