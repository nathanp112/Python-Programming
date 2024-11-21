# Task 5

import os


def main():
    os.makedirs("d1/d2/d3", exist_ok=True)
    open("d1/file.txt1", "a")
    open("d1/file.txt2", "a")
    # d2
    open("d1/d2/file1.txt", "a")
    open("d1/d2/file2.txt", "a")
    # d3
    open("d1/d2/d3/file1.txt", "a")
    open("d1/d2/d3/file2.txt", "a")


if __name__ == "__main__":
    main()
