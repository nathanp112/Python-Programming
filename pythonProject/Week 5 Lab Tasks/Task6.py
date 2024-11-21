start = int(input("Please enter starting number: "))
end = int(input("Please enter ending number: "))
increment = int(input("Please enter increment number: "))

for i in range(0, start+1):
    print("Output 1: ", i)
for i in range(1, start+1):
    print("Output 2: ", i)
for i in range(start, end+1):
    print("Output 3: ", i)
for i in range(start, end+1, increment):
    print("Output 4: ", i)