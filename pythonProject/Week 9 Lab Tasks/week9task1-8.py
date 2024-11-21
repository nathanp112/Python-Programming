# Task 1
import re
text = " "
number = 1000
username = "admin"
userid = 12345
password = "a8e3l6$#"
email = "ex@ex.ex"

# Task 2
reg_empty = r'\s'
print("Task 2:", bool(re.match(reg_empty, text)))

# Task 3
reg_min_10chars = r'^.{10,}+$'
print("Task 3:", bool(re.match(reg_min_10chars, text)))

# Task 4
reg_non_alpha = r'^\W+$'
print("Task 4:", bool(re.match(reg_non_alpha, text)))

# Task 5
reg_only_alpha = r'^[a-zA-Z_]+$'
print("Task 5:", bool(re.match(reg_only_alpha, username)))

# Task 6
reg_only_digit = r'^\d+$'
print("Task 6:", bool(re.match(reg_only_digit, str(userid))))

# Task 7
reg_password = r'^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[!"#$%&/]).+$'
print("Task 7:", bool(re.match(reg_password, password)))

# Task 8
reg_email = r'^[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+$'
print("Task 8:", bool(re.match(reg_email, email)))
