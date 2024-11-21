# Student ID: 101485672
# Student Name: Nathan Prince

numbers = [73, 18, 64, 60, 26, 33, 66, 74, 59, 69, 60, 95, 53, 45, 57, 1, 48, 88, 13, 62]
for num in numbers:
    if num >=1 and num <= 50:
        with open("50_and_under.txt", "a") as f:
            f.write(str(num) + '\n')
    elif num >= 51 and num <= 100:
        with open("50_and_over.txt", "a") as f:
            f.write(str(num) + '\n')


