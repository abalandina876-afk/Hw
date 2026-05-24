try:
    number = int(input("Enter a number: "))
    print("Converted number:", number)
except ValueError:
    print("These data cannot be converted to a number")