path = "C:\\Users\\Dell\\Downloads\\CSB42\\Day10\\myText.txt"

import os
if os.path.exists(path):
    print("File nay duoc ton tai")
else:
    print("File ko ton tai")

    # with open(path, "r") as file:
        # read(): Trả về string và hiện ra toàn bộ text trong file
        # currentLines = file.readlines()
        # print(currentLines)
        # Trả về 1 mảng gồm tất cả các dòng trong file(giá trị cũ)
        # print("content: ", currentLines)
        # for i in range(0, len(currentLines)):
        #     print(f"{i + 1}, {currentLines[i].replace("\n", "")}")
        # Print theo dạng có số thứ tự đằng trước mỗi dòng
        # VD: 1, ...
        #     2, ...
        # file.close()


# with open(path, "w") as file:
#     # file.write("abc\n")
#     # file.write("abc\n")
#     # file.write("abc")

#     # Yêu cầu người dùng nhập 1 số n:
#     # Hiện ra n input để cho người dùng khai báo các dòng 1 ghi
#     # Sau khi ghi thì sẽ được lưu vào file
    # newLines = []
    # n = int(input("Nhập số lượng phần tử muốn ghi: "))
    # for i in range(0, n):
    #     value = input(f"Nhập dòng thứ {i + 1}")
    #     addDropLine = value + "\n"
    #     newLines.append(addDropLine)
    # finalLines  = currentLines + newLines
    # file.writelines(finalLines)
    # file.close()

# Tạo ra 1 hàm cho phép người dùng nhập nối tiếp thông tin nào trong file
# mà không bị mất đi các giá trị trước đó

# with open(path, "a") as file:
#     file.writelines(["ccc\n","ooo\n"])
#     file.close()


# Update file
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
def Add():
    new_value = input("Nhập giá trị mới: ")
    content.append(new_value+"\n")
def Update():
    index = int(input("Nhập index: "))
    new_value = input("Nhập giá trị mới: ")
    content[index - 1] = new_value + "\n"
def Delete():
    index = int(input("Nhập index: "))
    content.pop(index - 1)
def All():
    with open(path, "r") as file:
        content = file.readlines()
        for i in range(0, len(content)):
            print(f"{i + 1}, {content[i].replace("\n", "")}")
            file.close()
def Tong():
    with open(path, "r") as file:
        content = file.read()
        tong = len(content)
        print(tong)
while True:
    print("--------------")
    print("[1].Thêm")
    print("[2].Sửa")
    print("[3].Xóa")
    print("[4].Đọc")
    print("[5].Tổng số lượng chữ cái trong file")
    print("[0].Thoát")
    choice = input("Chọn chức năng: ")
    with open(path, "r") as file:
        content = file.readlines()
        file.close()
        if choice == "1":
            Add()
        elif choice == "2":
            Update()
        elif choice == "3":
            Delete()
        elif choice == "4":
            All()
        elif choice == "5":
            Tong()
        elif choice == "0":
            break
        with open(path, "w") as file:
            file.writelines(content)
            file.close()