# Student ID: 101485672
# Student Name: Nathan Prince
# 1) Ask the user for a path value. (0.5 marks)
# a) Determine if the path exists in the current filesystem (2 marks)
# message should be printed to system’s standard error (0.5 marks)
# ii) If so, proceed to Step 2
# 2) Calculate and output the total number of
# i) All files and folders (1 mark)
# ii) Just the number of files (1 mark)
# iii) Just the number of directories (1 mark

import os
import sys


def count_files_and_dirs(path):
    if not os.path.exists(path):
        raise FileNotFoundError("The path not found")

    # Point 2
    total_count = 0
    files_count = 0
    folders_count = 0
    for root, dirs, files in os.walk(path):
        folders_count += len(dirs)
        total_count += len(files)

    folders_count += 1

    total_count = folders_count + files_count
    return total_count, folders_count, files_count


try:
    path = input("Enter the path:")
    total_count, folders_count, files_count = count_files_and_dirs(path)
    print("Total number of files and directories is", total_count)
    print("Total number of files", files_count)
    print("Total number of folders", folders_count)
except FileNotFoundError as Err:
    print("Error", Err, file=sys.stderr)
