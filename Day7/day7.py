# Function trong python: 
# - Dùng để thực thi 1 khối câu lệnh nào đó
# - Tái sử dụng lại ở nhiều chỗ
# Cách viết: def ten_ham():
# Cách để thực thi hàm là phải gọi lại hàm

# Void: In ra gì đó hoặc thay đổi 1 điều gì đó
a = 10
def do_something():
    global a
    a = 100
    print("Hôm nay trời HN khá rét")

# do_something()
# print(a)

# Return: Trả về 1 giá trị nào đó được viết trong hàm
def count_plus():
    return 10 + 10

# print(count_plus())

# Params: tham số của hàm, có thể có nhiều hơn 1 tham số
# Mình có thể gán giá trị mặc định cho tham số khi mà lúc gọi hàm ta ko khai báo
# def f(x = 2, y = 1):
#     return x ** 2 + 2 * x + 3 + y * 2

# print(f())

# Tạo 1 function có 3 tham số lượt là: số thứ 1, số thứ 2, phép tính
# Khi gọi hàm thì kết quả phép tính sẽ được thực thi dựa theo những tham số mà người dùng khai báo

def calculator(n1, n2, phep_tinh):
    if phep_tinh == "+":
        return n1 + n2
    elif phep_tinh == "-":
        return n1 - n2
    elif phep_tinh == "*":
        return n1 * n2
    elif phep_tinh == "/":
        return n1 / n2
    else:
        return "Phép tính không hợp lệ"

# n1 = int(input("Enter n1: "))
# n2 = int(input("Enter n2: "))
# phepTinh = input("Enter operator: ")

# print(calculator(n1, n2, phepTinh))

foods = []
# Tao 1 chương trình quản lý 1 mảng món ăn
# Tạo ra 4 function để xử lý các chức năng: Create, update, delete, read

# Creat: dùng để thêm mới 1 giá trị vào mảng
# VD: def create(newValue)

# Update: Thay thế 1 món ăn nào đó nằm trong mảng
# VD: def update(position, newValue)

# Delete: Xoá 1 phần thử bất kỳ nằm trong mảng
# VD: def delete(position, clear=False)

# Read: Đọc full dữ liệu nằm trong mảng và in ra theo dạng:
# VD: def read():
# 1. món thứ 1
# 2. món thứ 2 
# 3. ...


# VD:# food = ["Bun chan", "Pho", "rau", "chuoi"]
# food[position] = "tom"
# print(food)

        # food.remove("Pho") => food = ["Bun cha", "rau", "chuoi"]
        # food[position]  = "Tom" => food = ["Bun cha", "tom", "chuoi"]

# i = 0   
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i = i + 1

Foods = []

def create(food):
    Foods.append(food)
def update(position, food):
    Foods.pop(position)
    Foods.insert(position,food)
def delete(position, clear = False):
    Foods.pop(position)
def read():
    i = 1
    for food in Foods:
        print(f"{i}, {food}")
        i += 1

while True:
    print("--------------")
    print("[1]. Create")
    print("[2]. Update")
    print("[3]. Delete")
    print("[4]. Read")
    print("[0]. Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        newFood = input("Enter random food: ")
        create(newFood)
        print("Bạn vừa thực thi lựa chọn 1")
    elif choice == "2":
        print("Bạn vừa thực thi lựa chọn 2")
    elif choice == "3":
        print("Bạn vừa thực thi lựa chọn 2")
    elif choice == "4":
        read()
    elif choice == "0":
        print("Cam on ban da nhap lua chonnnnn !!!!")
        break