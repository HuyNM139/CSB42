# Phần 1:
# 1.
# def even(n):
#     return n % 2 == 0
# num = int(input("Input a number: "))
# if even(num):
#     print("This number is even")
# else:
#     print("This number is not even")

# 2.
# import math
# def cal_area(radius):
#     return math.pi * (radius ** 2)
# radius = float(input("Input radius: "))
# area = cal_area(radius)
# print(f"Circle's area: {round(area, 2)}")

# 3.
# def reverse_str(s):
#     return s[::-1]
# text = input("Input a text: ")
# reversed_text = reverse_str(text)
# print(f"Reversed text: {reversed_text}")

# 4.
# def palindrome(s):
#     return s == s[::-1]
# text = input("Input a text: ")
# if palindrome(text):
#     print("This is a palindrome.")
# else:
#     print("This is not a palindrome.")

# Phần 2:
# 1. 
# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     return fact
# num = int(input("Input a number: "))
# print(f"{num}! = {factorial(num)}")

# 2.
# num_list = [5, 1, 8, 92, -1, 30]
# print("Original List:")
# for num in num_list:
#     print(num, end=' ')
# for i in range(len(num_list)):
#     for j in range(i + 1, len(num_list)):
#         if num_list[j] < num_list[i]:
#             num_list[i], num_list[j] = num_list[j], num_list[i]
# print("\nSorted List:")
# for num in num_list:
#     print(num, end=' ')

# 3.
# def print_fibo(n):
#     a, b = 1, 1
#     for _ in range(n):
#         print(a, end=" ")
#         a, b = b, a + b
# n = int(input("Input a number: "))
# print(f"First {n} Fibonacci numbers:")
# print_fibo(n)

# Phần 3:
import os
import msvcrt
def tao_map():
    game_map = [
        ["P","-","-","-","-","-","-","-","-","-"],
        ["-","-","-","-","-","K","-","-","-","-"],
        ["-","-","-","-","-","-","-","-","-","-"],
        ["D","-","-","-","-","-","-","-","-","-"],
        ["-","-","-","-","-","-","-","-","-","-"]
    ]
    return game_map
def vi_tri(game_map):
    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            if game_map[i][j] == "P":
                return i,j
def in_map(game_map):
    for d in game_map:
        print(" ".join(d))
def huong_di(ch):
    if ch == "w":
        return -1,0
    elif ch == "s":
        return 1,0
    elif ch == "a":
        return 0,-1
    elif ch == "d":
        return 0, 1
    return 0, 0
def di_chuyen(game_map, co_khoa):
    x, y = vi_tri(game_map)
    ch = msvcrt.getch().decode('utf-8')
    dx, dy = huong_di(ch)
    nx = x + dx
    ny = y + dy
    if nx < 0 or nx >= len(game_map) or ny < 0 or ny >= len(game_map[0]):
        return co_khoa, False
    if game_map[nx][ny] == "K":
        co_khoa = True
        print("Ban da nhat duoc khoa!")
    if game_map[nx][ny] == "D":
        if co_khoa:
            print("Ban thang!")
        else:
            print("Ban thua! Chua lay khoa")
        return co_khoa, True
    game_map[x][y] = "-"
    game_map[nx][ny] = "P"
    return co_khoa, False
game_map = tao_map()
co_khoa = False
ket_thuc = False
while not ket_thuc:
    os.system("cls")
    print("== THE ESCAPE GAME ==")
    print("Use W A S D to move (P)layer.")
    print("Find (K)ey first then exit through (D)oor.")
    in_map(game_map)
    co_khoa, ket_thuc = di_chuyen(game_map, co_khoa)
    print("Game over")