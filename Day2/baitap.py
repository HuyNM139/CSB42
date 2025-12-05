def avg(numbers):
    even_numbers=[num for num in numbers if num% 2 == 0]
    if even_numbers:
        return sum(even_numbers)/len(even_numbers)
    else:
        return 0
input_numbers= input("Nhập vào một danh sách số nguyên: ")
numbers = list(map(int, input_numbers.split()))
average = avg(numbers)
print(f"Trung bình các số chẵn trong danh sách là: {average}")