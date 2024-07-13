print("1. Convert inches -> cm")
print("2. Convert cm -> inches")

choice = input("Make your selection (1,2): ")

if choice == "1":
    inches = int(input("Enter inches: "))
    cm = inches * 2.54
    print("Number of cm:", cm),
elif choice == "2":
    cm = int(input("Enter cm: "))
    inches = cm / 2.54
    print("Number of inches:", inches),
else:
    print("Invalid selection. Please run the program again and choose 1 or 2.")

