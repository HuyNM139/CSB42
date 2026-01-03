# Bai 1
# n = int(input("Input number: "))
# for i in range(1, n+1):
#     print("#" * i)

# Bai 2
# while True:
#     a = float(input("Input a positive number: "))
#     if a > 0:
#         print("Thank you.")
#         break

# Bai 3
# n = int(input("Input number: "))
# if n < 0:
#     print("Invalid")
# elif n == 0:
#     print("0! = 1")
# else:
#     giaithua = 1
#     for i in range(1, n+1):
#         giaithua *= i
#     print(f"{n}! = {giaithua}")

# Bai 4
# n = int(input("Input number: "))
# total = sum(int(i) for i in str(n))
# print(f"Sum of digits of {n} = {total}")

# Bai 5
# print("Numbers with sum of digits = 9:")
# count = 0
# num = 1000
# while count < 10:
#     if sum(int(i) for i in str(num)) == 9:
#         print(num, end=' ')
#         count += 1
#     num += 1

# Bai 6
# import turtle
# n = int(input("Input number of edges: "))
# if n > 2:
#     for _ in range(n):
#         turtle.forward(100)
#         turtle.left(360 / n)
#     turtle.done()
# else:
#     print("Number of edges must be > 2")

# Bai 7
# import turtle
# r = 5
# for i in range(50):
#     turtle.circle(r, 180)
#     r += 2
# turtle.done()