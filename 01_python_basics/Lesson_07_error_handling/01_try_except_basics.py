

text = input("Enter a number: ")

try:
    number = int(text)
except ValueError:
    print("That was not a valid number.")
    number = None
else:
    print("Conversion succeeded.")
finally:
    print("This always runs.")

if number is not None:
    print(f"Using number: {number}")