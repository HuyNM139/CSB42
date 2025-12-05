# 6. Phép so sánh trong python: >, <, >=, <=, ==, !=
# Lồng điều kiện: &&, || => python: and , or
# Khi áp dụng điều kiện này thì giá trị trả về là gì ? => True/False

a = 10
b = 20

c = a < b
print("Kết quả song sánh:" + str(c))

# if/else: câu điều kiện
if a < b:
    print("A < B")
elif a == b:
    print("A = B")
else: #trường hợp còn lại khi mà không cái if nào đúng
    print("B > A")

#Nhập vào input 1 tên:
# Trong lớp có 3 bạn được giải:
# Bảo -> nhất
# Minh Huy -> nhì
# Tùng Anh -> ba
# a = input("Nhập tên 1 bạn: ")
# if a == "Bảo":
#     print("Bảo được giải nhất")
# elif a== "Minh Huy":
#     print("Huy được giải nhì")
# elif a== "Tùng Anh":
#     print("Tùng Anh được giải ba")
# else:
#     print("Khong co ten nay trong danh sach")

#Bài 124
# sodiem = float(input("Nhập điểm số: "))
# if sodiem >= 9:
#     print("A+")
# elif sodiem >= 8:
#     print("A")
# elif sodiem >= 7:
#     print("B")
# elif sodiem >= 6:
#     print("C")
# elif sodiem >= 5:
#     print("D")
# elif sodiem <5:
#     print("E")
# else:
#     print("-1")

#Bài 102
# a = str(input("Nhập số a: "))
# b = str(input("Nhập số b: "))
# c = str(input("Nhập số c: "))
# d = str(input("Nhập số d: "))

# if a<b and a<c and a<d:
#     if b<c and b<d:
#         print("Số nhỏ thứ nhì là:" + b)
#     elif c<b and c<d:
#         print("Số nhỏ thứ nhì là:" + c)
#     else:
#         print("Số nhỏ thứ nhì là:" + d)

#Bài 125
# import math
# a = float(input("Nhập số a: "))
# b = float(input("Nhập số b: "))
# c = float(input("Nhập số c: "))

# delta = b*b - 4*a*c

# if delta < 0:
#     print("No solution")
# else:
#     d = math.sqrt(delta)
#     x1 = (-b - d) / (2 * a)
#     x2 = (-b + d) / (2 * a)
#     if x1 > x2:
#         x1, x2 = x2, x1
#     print(round(x1,2), round(x2,2))

#Bai 107
# x1 = float(input("Nhập số nguyên x1: "))
# y1 = float(input("Nhập số nguyên y1: "))
# x2 = float(input("Nhập số nguyên x2: "))
# y2 = float(input("Nhập số nguyên y2: "))
# x3 = float(input("Nhập số nguyên x3: "))
# y3 = float(input("Nhập số nguyên y3: "))
# line = x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)
# if line == 0:
#     print(1)
# else:
#     print(0)