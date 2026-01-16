# list_person = [
#     {
#         "name": "Alice",
#         "age": 30,
#         "city": "New York"
#     },
#     {
#         "name": "Danh Phuong",
#         "age": 24,
#         "city": "Ha Noi"
#     }
# ]
list_person = [
    {
        "id": 1,
        "full_name": "Nguyen Van A",
        "age": 25,
        "gender": "male"
    },
    {
        "id": 2,
        "full_name": "Tran Thi B",
        "age": 23,
        "gender": "female"
    },
    {
        "id": 3,
        "full_name": "Le Hoang C",
        "age": 28,
        "gender": "male"
    },
    {
        "id": 4,
        "full_name": "Pham Ngoc D",
        "age": 26,
        "gender": "female"
    },
    {
        "id": 5,
        "full_name": "Vo Minh E",
        "age": 30,
        "gender": "male"
    },
    {
        "id": 6,
        "full_name": "Dang Thi F",
        "age": 24,
        "gender": "female"
    },
    {
        "id": 7,
        "full_name": "Bui Quang G",
        "age": 27,
        "gender": "male"
    },
    {
        "id": 8,
        "full_name": "Hoang Lan H",
        "age": 22,
        "gender": "female"
    }
]
# In ra tên của thầy
# print(list_person[1]["name"])
# # Viết 3 input để update lại dictionary person trên
# Ket qua:
# new_name = input("name: ")
# new_age = int(input("age: "))
# new_city = input("city: ")
# list_person.update({"name": new_name})
# list_person.update({"age": new_age})
# list_person.update({"city": new_city})
# print(list_person)

# Yeu cau 2:
# Tạo ra thêm 1 input cho phép người dùng chọn dictionary muốn thay đổi nằm trong list
# lựa chọn chỉ có hiện ra là 1 hoặc 2
# Nếu chọn 1 thì update thằng đầu tiên
# Sau khi chọn xong thì hiện ra 3 input để update person tại vị trí mình chọn
# chon = int(input("Chọn người cần sửa (1 hoặc 2): "))
# index = chon - 1
# new_name = input("name: ")
# new_age = int(input("age: "))
# new_city = input("city: ")
# list_person[index]["name"] = new_name
# list_person[index]["age"] = new_age
# list_person[index]["city"] = new_city
# print(list_person)

# [1]. Add thêm person vào list_person
# - Hiện ra 3 input cho phép người dùng khai báo 1 person mới
# [2]. In ra toàn bội person đang theo dạng:
# => 1. person1 - age1 - gender1
#    2. person2 - age2 - gender2
#    .....
# [3]. Update lại giá trị của 1 person bất kỳ nằm trong list_person
# Cho phép người dùng nhập 1 id bất kỳ muốn thay đổi thông tin:
# Hiện ra lần lượt 3 input để input 
# [4]. Xóa 1 person bất kỳ nằm trong list dựa theo input người dùng
# [5]. Sắp xếp lại list dựa theo age (thứ tự tăng dần)
# [0]. Thoát chương trình
# Chú ý phải tạo ra 5 hàm cho 5 lựa chọn trên
def add():
    fullname = input("Nhập họ và tên: ")
    age = int(input("Nhập tuổi: "))
    gender = input("Nhập giới tính: ")
    id = len(list_person) + 1
    list_person.append({
        "id": id,
        "full_name": fullname,
        "age": age,
        "gender": gender
    })
def show():
    for person in list_person:
        print(f"{person["full_name"]} - {person["age"]} - {person["gender"]}")
def update():
    id_update = int(input("Nhập id: "))
    for person in list_person:
        if person["id"] == id_update:
            person["full_name"] = input("Nhập tên mới: ")
            person["age"] = input("Nhập tuổi mới: ")
            person["gender"] = input("Nhập giới tính mới: ")
            break
def delete():
    id_delete = int(input("Nhập id: "))
    for person in list_person:
        if person["id"] == id_delete:
            list_person.remove(person)
            break
def sort():
    for i in range(len(list_person)):
        for j in range(i + 1, len(list_person)):
            if list_person[i]["age"] > list_person[j]["age"]:
                temp = list_person[i]
                list_person[i] = list_person[j]
                list_person[j] = temp
while True:
    print("1. Add person")
    print("2. Hiện danh sách")
    print("3. Update person")
    print("4. Xóa person")
    print("5. Sắp xếp theo age")
    print("0. Thoát")
    choice = input("Chọn: ")
    if choice == "1":
        add()
    elif choice == "2":
        show()
    elif choice == "3":
        update()
    elif choice == "4":
        delete()
    elif choice == "5":
        sort()
        show()
    elif choice == "0":
        break