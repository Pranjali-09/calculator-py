import math

active = True  # Program switch

while active:
    print("1) Add")
    print("2) Subtract")
    print("3) Divide")
    print("4) Multiply")
    print("5) Squared")
    print("6) Square Root")
    print()
    print("0) Exit")

    answer = int(input("Option: "))  # Will crash if non-number entered
    print()

    if answer == 1:
        first = float(input("First Number: "))
        second = float(input("Second Number: "))
        final = first + second
        print("Answer:", float(final))
        print()

    elif answer == 2:
        first = float(input("First Number: "))
        second = float(input("Second Number: "))
        final = first - second
        print("Answer:", float(final))
        print()

    elif answer == 3:
        first = float(input("First Number: "))
        second = float(input("Second Number: "))
        final = first / second
        print("Answer:", float(final))
        print()

    elif answer == 4:
        first = float(input("First Number: "))
        second = float(input("Second Number: "))
        final = first * second
        print("Answer:", float(final))
        print()

    elif answer == 5:
        first = float(input("Number: "))
        final = first * first
        print("Answer:", float(final))
        print()

    elif answer == 6:
        first = float(input("Number: "))
        final = math.sqrt(first)
        print("Answer:", float(final))
        print()

    elif answer == 0:
        active = False

    else:
        print("Please select a valid option number\n")
