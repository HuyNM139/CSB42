n = int(input("Nhập số nguyên dương n: "))
tong_le = 0
for i in range(1, n+1):
    if i % 2 == 1:
        tong_le += i
nguyen_to = True
if n < 2:
    nguyen_to = False
else:
    for i in range(2, n):
        if n % i == 0:
            nguyen_to = False
            break
print("Tổng các số lẻ từ 1 đến", n, "là:", tong_le)
if nguyen_to:
    print(n, "là số nguyên tố")
else:
    print(n,"không phải là số nguyên tố")
print("Các ước số của", n, "là:")
for i in range(1, n+1):
    if n % i == 0:
        print(i)