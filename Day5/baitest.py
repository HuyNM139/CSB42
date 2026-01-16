# Phan 1
# Bai 1
# first_name = input("First Name: ")
# last_name = input("Last name: ")
# print(f"Your full name is {first_name} {last_name}")
# Bai 2
# user_input = input("Your input: ")
# print(f"Capitalized: {user_input.upper()}")
# Bai 3
# num = float(input("Input a number: "))
# print(f"Squared input: {num ** 2}")
# Bai 4
# import turtle
# radius = int(input("Input circle's radius: "))
# turtle.circle(radius)

# Phan 2
# Bai 1
# for i in range(3,13):
#     print(i)
# Bai 2
# n = int(input("Input a number: "))
# for i in range(n+1):
#     print(i)
# Bai 3
# n = int(input("Input a number: "))
# for i in range(1, n + 1,2):
#     print(i)
# Bai 4
# import turtle
# edges = int(input("Input number of edges: "))
# for i in range(edges):
#     turtle.forward(100)
#     turtle.right(360/edges)

# Phan 3
# Bai 1
# num = float(input("Input a number: "))
# if num > 13:
#     print("This number is larger than 13")
# else:
#     print("This number is not larger than 13")
# Bai 2
# num = float(input("Input a number: "))
# if num % 2==0:
#     print("This number is even")
# else:
#     print("This number is not even")
# Bai 3
# month = int(input("Input a month: "))
# if month in {1,3,5,7,8,10,12}:
#     print("This month has 31 days")
# elif month in {4,6,9,11}:
#     print("This month has 30 days")
# elif month == 2:
#     print("This month has 28 or 29 days")
# else:
#     print("Is not a month")

# Phan 4
# Bai 1
# username = input("Username: ")
# password = input("Password: ")
# email = input("Email: ")
# print("Registered successfully.")
# Bai 2
# username = input("Username: ")
# password = input("Password: ")
# while True:
#     repeat_password = input("Repeat password: ")
#     if password == repeat_password:
#         email = input("Email: ")
#         print("Registered successfully.")
#         break
#     else:
#         print("Passwords not match. Please input again.")
# Bai 3
# username = input("Username: ")
# while True:
#     password = input("Password: ")
#     if len(password) < 8:
#         print("Invalid password. Please input again.")
#     else:
#         break
# while True:
#     repeat_password = input("Repeat password: ")
#     if password == repeat_password:
#         break
#     else:
#         print("Passwords not match. Please input again.")
# while True:
#     email = input("Email: ")
#     if "@" in email and "." in email:
#         print("Registered successfully.")
#         break
#     else:
#         print("Invalid email. Please input again.")

# Phan 5:
# import random
# score = 0
# for i in range(4):
#     num1 = random.randint(1, 20)
#     num2 = random.randint(1, 20)
#     op=random.choice(['+', '-', '*', '/'])
#     if op== '+':
#         correct_ans = num1 + num2
#     elif op == '-':
#         correct_ans = num1 - num2
#     elif op == '*':
#         correct_ans = num1 * num2
#     else:
#         correct_ans = round(num1 / num2, 2)
#     ans = float(input(f"{num1} {op} {num2} = "))
#     if ans == correct_ans:
#         print("1 for True, 0 for False: 1")
#         score += 1
#         print(f"Score: {score}")
#     else:
#         print("1 for True, 0 for False: 0")
#         print("Incorrect")
# print(f"Game over! Your score is {score}")
a = "MindX"
print(str(a))