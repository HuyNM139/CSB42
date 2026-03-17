# Bai 1
# def is_int(num):
#     return num == int(num)
# num = float(input("Input number: "))
# if is_int(num):
#     print(f'{int(num)} is an integer')
# else:
#     print(f'{num} is not an integer')

# Bai 2
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True
# n = int(input("Input number: "))
# print(f'{n} is a prime' if is_prime(n) else f'{n} is not a prime')

# Bai 3
# n = int(input())
# count = 0
# num = 2
# while count < n:
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         print(num, end=' ')
#         count += 1
#     num += 1

# Bai 4
# n = int(input())
# def factorial(x):
#     f = 1
#     for i in range(1, x+1):
#         f *= i
#     return f
# s = 0
# for i in range(1, n+1):
#     s += factorial(i) / i
# print(int(s))

# Bai 5
from datetime import datetime
now = datetime.now()
print("Today is", now.strftime('%d/%m/%Y'))
print("Time right now:", now.strftime('%H:%M:%S'))
