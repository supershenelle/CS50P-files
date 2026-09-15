import string

def main():
    plate = input("Plate: ")
    plate = plate.upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def check_digit(s):
    valid = True
    for index, char in enumerate(s):
         if char.isdigit():
            if char == '0':
                return False

            digit = int(index)
            check = s[digit:]

            if check.isdigit():
                return True
            else:
                return False

    return valid

def punc(s):
    valid = True
    punctuation_marks = string.punctuation

    for char in s:
            if char in punctuation_marks or char in[" ", "."]:
                valid = False

    return valid

def is_valid(s):
    valid = True

    if not 2 <= len(s) <= 6:
        valid = False

    elif not (s[0].isalpha() and s[1].isalpha()):
        valid = False

    if not check_digit(s) or not punc(s):
        valid = False

    return valid

main()
