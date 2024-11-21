# -Store all the files and folders of the current working directory
# -Output each file/directory on a new line

import os


def main():
    filenames = os.listdir()
    for filename in filenames:
        print("Files/Directories:", filename)


if __name__ == '__main__':
    main()
