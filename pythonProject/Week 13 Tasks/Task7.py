import sys


def main():
    try:
        number = int(input("Enter a number:"))
        if number % 2 != 0:
            print("You entered:", number)
        else:
            print("The number is even")
    except ValueError as e:
        print("Error", e, file=sys.stderr)
    finally:
        print("Thank you for using the program")


if __name__ == "__main__":
    main()
