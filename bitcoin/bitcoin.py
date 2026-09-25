import requests
import sys

argcount = len(sys.argv)
userarg = argcount - 1

try:
    if not userarg == 1:
         raise requests.RequestException("Missing command-line argument")

    elif sys.argv[1].isalpha():
        raise requests.RequestException("Command-line argument is not a digit")

    else:
        url = "https://rest.coincap.io/v3/assets/bitcoin"
        headers = {"Authorization": "Bearer 17cd01ccd707daafe34592cdeee7c183a3585618f211f4ea9ab03e101011de7c"}
        response = requests.get(url, headers=headers)
        content = response.json()

        price = content["data"]["priceUsd"]
        price = float(price) * float(sys.argv[1])
        print(f"${float(price):,.4f}")

except requests.RequestException as e:
    sys.exit(f"{e}")
