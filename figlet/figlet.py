import sys
from pyfiglet import Figlet
import random
figlet = Figlet()

fonts = figlet.getFonts()

try:
    if len(sys.argv) == 0:
        figlet.setFont(font=fonts[random.choice(fonts)])

    elif len(sys.argv) == 3:
        figlet.setFont(font=sys.argv[2])

except (IndexError, ValueError):
     sys.exit("Invalid usage")

i = input("Input: ")
print("Output: ")
print(figlet.renderText(i))
