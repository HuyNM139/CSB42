# text = "Lrrrrrrrrrr ffff dsfsfs fsdfsfsf"
# text = "Referencet"
# len(tên_chuỗi) => in ra số lượng ký tự trong 1 chuỗi
# Truy cập vào các vị trí nằm trong 1 chuỗi: tên_chuỗi[index]
# Note: 0 <= index < len(tên_chuỗi)
# Cắt chuỗi: tên_chuỗi[start: end] => lấy trong khoảng bắt đầu và kết thúc
# start <= text < end
# Trỏ vào phần tử cuối cùng nằm trong 1 chuỗi: tên_chuỗi[len(tên_chuỗi) - 1]
# print("Length: "+str(len(text)))
# giá trị của length sẽ luôn lớn hơn vị trí cuối cùng của chuỗi 1 đơn vị
# print(text[9])

# Bài 1. Cho phép nhập 2 input start và end
# => In ra chuỗi trong khoảng start và end

# text = "Reference site about Lorem Ipsum"
# start = int(input("Nhập start: "))
# end = int(input("Nhập end: "))
# print(text[start:end])


# Bài 2. Cho phép người dùng thêm 1 ký tự bất kỳ vào trong chuỗi
# Có 2 input:
# - 1: hiện ra vị trí muốn thêm
# - 2: Nhập 1 ký tự muốn thêm

# Cách 1:
# text = "Reference site about Lorem Ipsum"
# vitri = int(input("Nhập vị trí muốn thêm: "))
# kytu = input("Nhập 1 ký tự muốn thêm: ")
# text = text[:vitri] + kytu + text[vitri:]
# print(text)

# Cách 2:
# text = "Reference site about Lorem Ipsum"
# position = int(input("Enter position: "))
# left = text[0: position]
# right = text[position: ]
# print(left)
# print(right)

# newValue = input("Enter new value: ")
# result = left + newValue + right
# print(result)


# Bài 3: Check xem ký tự có tồn tại trong text không ?
# input: nhập 1 ký tự bất kỳ
# output: In ra "CÓ" nếu tồn tại và in ra "KHÔNG" nếu không tồn tại

# text = "Reference site about Lorem Ipsum"
# value = input("Nhập 1 ký tự: ")
# if value in text:
#     print("CÓ")
# else:
#     print("KHÔNG")


# Bài 4: Tìm kiếm số lần xuất hiện của 1 ký tự nằm trong chuỗi
# input: nhập 1 ký tự bất kỳ
# output: Đếm số lần xuất hiện của ký tự đó

# text = "Reference site about Lorem Ipsum"
# value = input("Nhập 1 ký tự: ")
# count = text.count(value)
# print(count)