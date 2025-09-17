num = input("Give me a number: ")
try:
    f = float(num)
    if f.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("That is not a valid number.")
