userInput = input("File name: ")
ans = userInput.strip().casefold()

if ans.endswith((".gif", ".jpg", ".jpeg", ".png")):
    if ans.endswith(".jpg"):
        print("image/jpeg")
    else:
        ftype = ans.rsplit(".", 1)[-1]
        print(f"image/{ftype}")

elif ans.endswith((".pdf", ".zip")):
    ftype = ans.rsplit(".", 1)[-1]
    print(f"application/{ftype}")

elif ans.endswith(".txt"):
    print("text/plain")

else:
    print("application/octet-stream")
