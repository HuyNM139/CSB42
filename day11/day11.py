path = "C:\\Users\\Dell\\Downloads\\CSB42\\day11\\text.txt"
import os
if os.path.exists(path):
    print("File nay duoc ton tai")
else:
    print("File ko ton tai")
# Yêu cầu người dùng nhập n, n là số lượng dòng mà người dùng muốn ghi vào file
# Sau khi nhập xong n, hiện ra n input để người dùng nhập thông tin vào file
# Sau khi nhập xong thì sẽ được lưu vào file 
# n = int(input("Nhập n: "))
# with open(path, "w") as file:
#     for i in range(n):
#         value = input(f"Nhập dòng thứ {i + 1}: ")
#         file.write(value + "\n")
#     file.close()
# Yêu cầu 2:
# Viết 1 input cho phép người dùng nhập 1 index bất kỳ nằm trong file
# Hiện ra input để người dùng nhập giá trị mới để thay thế giá trị dựa theo index
# with open(path, "r") as file:
#     content = file.readlines()
#     file.close()
# index = int(input("Nhập index: "))
# new_value = input("Nhập giá trị mới: ")
# content[index - 1] = new_value + "\n"
# with open(path, "w") as file:
#     file.writelines(content)
#     file.close()

# Yêu cầu 3:
# Cho phép người dùng nhập n person muốn điền vào file
# Mỗi person sẽ có 3 thông tin: name, age, address, point
# Sau khi nhập xong thì sẽ được lưu vào file theo dạng:
# name1 - age1 - address1 - point1
# name2 - age2 - address2 - point2
# ...
n = int(input("Nhập n person: "))
persons = []
for i in range(n):
    print(f"Nhập thông tin person {i + 1}: ")
    person = {}
    person["name"] = input("Tên: ")
    person["age"] = input("Tuổi: ")
    person["address"] = input("Địa chỉ: ")
    person["point"] = input("Điểm: ")
    persons.append(person)
with open(path, "a") as file:
    for person in persons:
        content = person["name"] + " - " + person["age"] + " - " + person["address"] + " - " + person["point"]
        file.write(content + "\n")