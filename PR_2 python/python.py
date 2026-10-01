# ==========================================================
# PROJECT: PATTERN GENERATOR AND NUMBER ANALYZER
# ==========================================================

print("=" * 55)
print("      WELCOME TO PATTERN GENERATOR AND NUMBER ANALYZER")
print("=" * 55)

while True:

    print("\nSelect an option:")
    print("1. Right-Angled Triangle")
    print("2. Pyramid")
    print("3. Left-Angled Triangle")
    print("4. Analyze a Range of Numbers")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # ------------------------------------------------------
    # 1. RIGHT-ANGLED TRIANGLE
    # ------------------------------------------------------
    if choice == "1":

        while True:
            try:
                rows = int(input("Enter the number of rows for the pattern: "))

                if rows <= 0:
                    print("Invalid row count! Please enter a positive number.")
                    continue

                break

            except ValueError:
                print("Please enter a valid integer.")

        print("\nPattern:")

        for i in range(1, rows + 1):
            for j in range(i):
                print("*", end=" ")
            print()

    # ------------------------------------------------------
    # 2. PYRAMID
    # ------------------------------------------------------
    elif choice == "2":

        while True:
            try:
                rows = int(input("Enter the number of rows for the pattern: "))

                if rows <= 0:
                    print("Invalid row count! Please enter a positive number.")
                    continue

                break

            except ValueError:
                print("Please enter a valid integer.")

        print("\nPattern:")

        for i in range(1, rows + 1):

            # Print spaces
            for j in range(rows - i):
                print(" ", end=" ")

            # Print stars
            for j in range(2 * i - 1):
                print("*", end=" ")

            print()

    # ------------------------------------------------------
    # 3. LEFT-ANGLED TRIANGLE
    # ------------------------------------------------------
    elif choice == "3":

        while True:
            try:
                rows = int(input("Enter the number of rows for the pattern: "))

                if rows <= 0:
                    print("Invalid row count! Please enter a positive number.")
                    continue

                break

            except ValueError:
                print("Please enter a valid integer.")

        print("\nPattern:")

        for i in range(1, rows + 1):

            # Print spaces
            for j in range(rows - i):
                print(" ", end=" ")

            # Print stars
            for j in range(i):
                print("*", end=" ")

            print()

    # ------------------------------------------------------
    # 4. NUMBER ANALYSIS
    # ------------------------------------------------------
    elif choice == "4":

        while True:
            try:
                start = int(input("Enter the start of the range: "))
                end = int(input("Enter the end of the range: "))

                if end <= start:
                    print("Invalid range! End must be greater than start.")
                    continue

                break

            except ValueError:
                print("Please enter valid integers.")

        total = 0

        print()

        for num in range(start, end + 1):

            # Odd / Even check
            if num % 2 == 0:
                print(f"Number {num} is Even")
            else:
                print(f"Number {num} is Odd")

            # Add number to total
            total += num

        print(f"\nSum of all numbers from {start} to {end} is: {total}")

    # ------------------------------------------------------
    # 5. EXIT
    # ------------------------------------------------------
    elif choice == "5":

        print("\nThank you for using Pattern Generator and Number Analyzer!")
        print("Program ended.")
        break

    # ------------------------------------------------------
    # INVALID CHOICE
    # ------------------------------------------------------
    else:
        print("Invalid choice! Please select a number from 1 to 5.")