# Bài 1
# number = int(input("Input number: "))
# if number % 2 == 0:
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")
# Bài 2
# num = float(input("Input number: "))
# if num == int(num):
#     print(f"{num} is an integer")
# else:
#     print(f"{num} is not an integer")
# Bài 3
# char = input("Input character: ")
# if len(char) == 1:
#     print(f"'{char}' is a digit")
# else:
#     print(f"'{char}' is not a digit")
# Bài 4
# n=int(input("Input number: "))
# if n%3==0 and n%5== 0:
#     print(f"{n} is divisible by 3 and 5")
# elif n % 3== 0:
#     print(f"{n} is divisible by 3")
# elif n% 5 == 0:
#     print(f"{n} is divisible by 5")
# else:
#     print(f"{n} is not divisible by 3 or 5")
# Bài 5
# print("Welcome to The Ultimate Security System")
# username = input("Username: ")
# password = input("Password: ")
# if username == "admin" and password == "12345":
#     print("You are logged in, admin.")
# else:
#     print("Wrong username or password.")
# Bài 6
# length1 = float(input("Input length 1: "))
# length2 = float(input("Input length 2: "))
# length3 = float(input("Input length 3: "))
# if length1 + length2 > length3 and length1 + length3 > length2 and length2 + length3 > length1:
#     print("The 3 line segments can form a triangle.")
# else:
#     print("The 3 line segments cannot form a triangle.")
# Bài 7
# length1 = float(input("Input length 1: "))
# length2 = float(input("Input length 2: "))
# length3 = float(input("Input length 3: "))
# if length1 + length2 <= length3 or length1 + length3 <= length2 or length2 + length3 <= length1:
#     print("The 3 line segments cannot form a triangle")
# elif length1 == length2 == length3:
#     print("The 3 line segments can form an equilateral triangle")
# elif length1*length1 + length2*length2 == length3*length3 or length1*length1 + length3*length3 == length2*length2 or length2*length2 + length3*length3 == length1*length1:
#     print("The 3 line segments can form a right triangle")
# else:
#     print("The 3 line segments can form a triangle")