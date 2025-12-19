# vòng lặp trong Python
# Sử dụng vòng lặp for khi biết trước số lần lặp hoặc khi duyệt qua các phần tử trong một tập hợp.
# Cú pháp:
# for biến_đếm in tập_hợp:
#     khối_lệnh

# Ví dụ sử dụng vòng lặp for để in các số từ 1 đến 5
# Chú ý: Hàm range(a, b) tạo ra một dãy số từ a đến b-1
# Ký tự [ biểu thị cho việc lớn hơn hoặc bằng, ký tự ) biểu thị cho việc nhỏ hơn.
# for i in range(1, 6): # 1, 2, 3, 4, 5 || [1,6)
#     print(i)

# Ví dụ sử dụng vòng lặp for để duyệt qua các phần tử trong một danh sách (list)
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# Sử dụng vòng lặp while khi không biết trước số lần lặp và cần lặp dựa trên một điều kiện.
# Cú pháp:
# while điều_kiện:
#     khối_lệnh

# Ví dụ sử dụng vòng lặp while để in các số từ 1 đến 5
# i = 1
# while i <= 5:
#     print(i)
#     i += 1  # Tăng biến đếm để tránh vòng lặp vô hạn

# bài tập vòng lặp
# Bài tập 1: Sử dụng vòng lặp for để tính tổng các số từ 1 đến 100 và in kết quả.
# in_sum = 0
# for i in range(1, 101):
#     in_sum += i
# print("Tổng các số từ 1 đến 100 là:", in_sum)

# bài tập 2: Sử dụng vòng lặp while để in các số chẵn từ 2 đến 20.
# i= 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# Bài 3: Sử dụng vòng lặp for để in tất cả các phần tử trong một danh sách các số nguyên.
# numbers = [10, 25, 30, 45, 50]
# for number in numbers:
#     print(number)

# Bài 4: Sử dụng vòng lặp while để yêu cầu người dùng nhập một số dương.
# Nếu người dùng nhập số âm hoặc số 0, yêu cầu họ nhập lại.
# num = -1
# while num <= 0:
#     num = int(input("Vui lòng nhập một số dương: "))
# print("Bạn đã nhập số dương:", num)


# Dictionary trong Python
# Dictionary (từ điển) là một cấu trúc dữ liệu trong Python dùng để lưu trữ các cặp khóa-giá trị.
# Mỗi khóa trong dictionary phải là duy nhất và được sử dụng để truy cập giá trị tương ứng.
# Cú pháp tạo một dictionary:
# my_dict = {
#     "key1": "value1",
#     "key2": "value2",
#     "key3": "value3"
# }

# Ví dụ tạo một dictionary và truy cập các giá trị
# student = {"name": "Alice", "age": 20, "major": "Computer Science"}

# Truy cập trong dictionary
# Truy cập giá trị bằng khóa
# print("Name:", student["name"])
# print("Age:", student["age"])

# Sử dụng phương thức items() để duyệt qua cả khóa và giá trị
# for key, value in student.items():
#     print(key, ":", value)

# print("items():", student.items())

# Cập nhật giá trị trong dictionary
# student["age"] = 21
# print("Updated age:", student["age"])

# Sử dụng update() để cập nhật
# student.update({"age": 21})
# student.update({"major": "Data Science", "age": 22})
# print("Updated student dictionary:", student)

# Thêm mới vào dictionary
# student["gpa"] = 3.8
# print("Updated student dictionary:", student)

# sử dụng update() để thêm mới
# student.update({"graduation_year": 2023})
# print("Updated student dictionary:", student)

# Xóa phần tử trong dictionary
# Sử dụng del để xóa một cặp khóa-giá trị
# del student["major"]
# print("Updated student dictionary after deletion:", student)

# Sử dụng pop() để xóa và trả về giá trị của khóa đã xóa
# removed_value = student.pop("age")
# print("Removed age:", removed_value)
# print("Updated student dictionary after pop:", student)

# sử dụng clear() để xóa tất cả các phần tử trong dictionary
# student.clear()
# print("Cleared student dictionary:", student)

# Sử dụng vòng lặp for để duyệt qua các khóa trong dictionary
# for key in student:
#     print(key, ":", student[key])

# print(len(student))  # In độ dài của dictionary (số cặp khóa-giá trị)

# Bài tập về Dictionary
# Bài tập 1: Tạo một dictionary để lưu trữ thông tin về một cuốn sách (tiêu đề, tác giả, năm xuất bản, số trang).
# book = {
#     "title": "All Tomorrows",
#     "author": "C. M. Kosemen",
#     "year_published": 2006,
#     "pages": 111
# }
# print(book)
# Bài tập 2: Tạo một dictionary chứa tên các loại trái cây và giá của chúng.
# Thực hiện:
# In giá của một loại trái cây bất kỳ.
# Thêm một loại trái cây mới.
# Cập nhật giá của một loại trái cây có sẵn.
# Khởi tạo dictionary trái cây với giá
# fruits = {
#     "cam": 30000,
#     "tao": 25000,
#     "chuoi": 20000
# }
# print("Giá táo:", fruits["tao"])
# fruits["oi"] = 15000
# fruits["chuoi"] = 22000
# print("Dictionary sau thay đổi:", fruits)
# Bài tập 3: Sử dụng vòng lặp for để in tất cả các khóa và giá trị trong dictionary đã tạo ở bài tập 1 hoặc 2.
# for fruit, price in fruits.items():
#     print(f"Trái cây: {fruit}, Giá: {price}")
# Bài tập 4: Viết một chương trình để đếm số lần xuất hiện của mỗi từ trong một câu nhập từ người dùng.
# Sử dụng dictionary để lưu trữ từ và số lần xuất hiện của chúng.
# sentence = input("Nhập câu của bạn: ").lower().split()
# counts = {}
# for word in sentence:
#     counts[word] = counts.get(word, 0) + 1
# for word, count in counts.items():
#     print(f"{word}: {count}")