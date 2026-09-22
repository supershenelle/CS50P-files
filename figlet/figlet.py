import sys
from pyfiglet import Figlet
import random
figlet = Figlet()

fonts = figlet.getFonts()

try:
    if len(sys.argv) == 1:
        figlet.setFont(font=random.choice(fonts))

    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        if sys.argv[2] in fonts:
            figlet.setFont(font=sys.argv[2])

        else:
            raise ValueError()

    else:
        raise IndexError()

except (IndexError, ValueError):
     sys.exit("Invalid usage")

i = input("Input: ")
print("Output: ")
print(figlet.renderText(i))
