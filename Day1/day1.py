# 1. Kiểu dữ liệu: string, int, float, boolean
# 2. Khai báo biến:
# Những điều cần lưu ý khi khai báo biến: Chú khi dùng ký tự đặc biệt trong biến
# Có 2 kiểu để khai báo biến: camel case, snake case => Khi tên biến đc cấu thành bởi từ 2 từ trở lên
# myWorkToday = "Done my job"
# my_work_today = "Done my job"
# a = "123"
# b = "456"
# print(a + " " + b)
# # Khai báo 5 biến liên quan đến 5 sở thích khác nhau
# a = "đi bơi"
# b = "lập trình"
# c = "chơi game"
# d = "nấu ăn"
# e = "đọc sách"
# print("favor: "+ a)
# print(f"favor: {a}") # template string cho phép thả biến vào trong string
# print(f"{a} - {b} - {c} - {d} - {e}")

# 3. Ép kiểu dữ liệu trong python
# number = "10"
# print(type(number))
# # number = int(number) # => 10
# # print(type(number))
# # k = 9
# # # k = str(k)
# # print("So yeu thich: "+ str(k))

# 4. Input trong python: là 1 hàm cho phép người dùng nhập dữ liệu từ bàn phím
# inputValue = input("Enter something here: ")
# print("Value: "+ inputValue)
# print(type(inputValue))

# fav1 = input("Sở thích của bạn: ")
# fav2 = input("Sở thích của bạn: ")
# fav3 = input("Sở thích của bạn: ")
# fav4 = input("Sở thích của bạn: ")
# fav5 = input("Sở thích của bạn: ")
# print("Sở thích: "+ fav1 + fav2+ fav3 + fav4+ fav5)
# print(type(fav1)) 

# 5. Toán tử trong python: +, -, *, /, **, %, //
# a = 10
# b = 3
# c= a + b
# c= a//3
# c=a**3

#Bài 1: Số gấp đôi
# inputValue = input("Số nguyên a: ")
# a= int(inputValue)
# if a <= 100:
#     print(f"Số nguyên thỏa mãn: {a * 2}")
# else:
#     print("Vui lòng nhập lại số")

#Bài 2
# inputa = input("Nhập số nguyên a: ")
# inputb = input("Nhập số nguyên b: ")
# inputc = input("Nhập số nguyên c: ")
# a = int(inputa)
# b = int(inputb)
# c = int(inputc)
# if a and b and c<= 100:
#     print(f"Input: {a} {b} {c}")
#     print(f"Output: {(a-b)*c}")
# else:
#     print("Vui lòng nhập lại số")

#Bai 7
# inputa = input("Nhập số nguyên a: ")
# inputb = input("Nhập số nguyên b: ")
# a = int(inputa)
# b = int(inputb)
# if a and b <= 1000:
#     print(f"Input: {a} {b}")
#     print(f"Output: {a + b + a*b}")
# else:
#     print("Vui lòng nhập lại số")

#Bai 38
# a = float(input("Nhập số:"))
# b = float(input("Nhập số:"))
# tong_lap_phuong = a**3 + b**3
# ket_qua = round(tong_lap_phuong, 2)
# print(ket_qua)