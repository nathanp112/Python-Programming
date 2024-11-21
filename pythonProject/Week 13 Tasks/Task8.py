import sys


def main():
    try:
        file_name = input("Please the  filename: ")
        if not file_name.endswith(".txt"):
            raise NameError("Filename name must be a text file")
        with open(file_name,"r") as file:
            print("Contents: ", file.read())
    except NameError as n:
        print("Name Error", n, file=sys.stderr)
    except FileNotFoundError as f:
        print("Error: File not found", f, file=sys.stderr)


if __name__ == "__main__":
    main()
