# listUser = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
# len(list): In ra số lượng phần tử có trong list 
# Các phần tử nằm trong list sẽ bắt đầu từ số 0
# Note: 0 <= index < len(list)
# Truy cập vào các phần tử bất kỳ trong list: Tên_list[index]
# Thêm 1 phần tử mới vào trong list: tên_list.append(newValue)

# print("So luong phan tu: ", len(listUser))
# print(listUser)
# print(listUser[0])
# print(listUser[len(listUser) - 1])

# thêm:
# listUser.append("Danh Phuong")
# print(listUser)

# Xoá 1 phần tử chỉ định
# listUser.remove("Charlie")

# Xoá phần tử cuối cùng trong list
# listUser.pop()
# print(listUser)


# listUser = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
# choice = input("Enter choice: ")
# if choice == "1":
#     value = input("Enter new value: ")
#     listUser.append(value)
#     print(listUser)
# elif choice == "2":
#     removeValue = input("Enter remove value: ")
#     if removeValue in listUser:
#         listUser.remove(removeValue)
#         print(listUser)
#     else:
#         print("Removed value is not existed")
# elif choice == "3":
#     index = int(input("Enter an index: "))
#     if index >=0 and index < len(listUser) - 1:
#         print(listUser[index])
#     else:
#         print("Index is not existed")
# else:
#     print(listUser)

# "1 + 2 + 3 + 4 + 5  + ... + n = tong"
# 1 + 2 + 3 + 5 = 6
# 1 + 2   5 + 
#     +   +
#     3 + 4
# value1 - value2 - value3 - value4
# Viết 1 cấu trúc if else:
# Sẽ có 1 input đầu vào: mời nhập các số bất kì từ 1 đến 4

# 1. Nhập để thêm thông tin mới vào trong list

# 2. Xoá 1 giá trị bât kỳ nằm trong list
# 3. Print ra 1 phần tử bất kỳ nằm trong list
# 4. In ra toàn bộ list

# 1. Phải có 1 input cho phép người dùng nhập các số bất kỳ bên trên

# s = ""
# s = s + "0" + " - " # s = "0 - "
# s = s + "1" + " - " # s = "0 - 1 - "
# s = s + "2" + " - " # s = "0 - 1 - 2 - "
# s = s + "3" + " - "
# s = s + "4" + " - "
# s = ""
# sum = 0

# for i in range(0, 5):
#     # s = s + str(i) + " - "
#     sum = sum + i
#     s = s + str(i)
#     # s = s + " - "
#     if i < 4:
#         s = s + " + "
# print(f"{s} = {sum}")


# value1 - value2
#    |        |
# value3 - value3


# Xoá phần tử đầu tiên ở trong list: không dùng hàm có sẵn
# list = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]

# for i in range(len(list)):
#     print(list[i])