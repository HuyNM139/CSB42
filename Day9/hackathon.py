# Bài 1
# # 1
# colors = ["blue","teal","green"]
# # 2
# print("Color list: ")
# for color in colors:
#     print(color)
# # 3
# new_color = input("Input a new color: ")
# colors.append(new_color)
# print("New color list: ")
# for color in colors:
#     print(color)

# Bài 2
# 1
# colors = ["blue","teal","green"]
# print("Color list: ")
# for color in colors:
#     print(color)
# pos = int(input("Input position: "))
# print(f"Color at position {pos}: {colors[pos-1]}")
# 2
# colors = ["blue","teal","green"]
# print("Color list: ")
# for color in colors:
#     print(color)
# delete_item = input("Item to delete: ")
# if delete_item in colors:
#     colors.remove(delete_item)
# else:
#     pos = int(delete_item)
#     colors.pop(pos-1)
# print("New color list: ")
# for color in colors:
#     print(color)

# Bài 3
# 1
# numbers = [5, 1,8,92,-1,30]
# find_number = int(input("Input a number: "))
# if find_number in numbers:
#     pos = numbers.index(find_number) + 1
#     print(f"Number found at position: {pos}")
# else:
#     print("Number not found")
# 2
# numbers = [5, 1,8,92,-1,30]
# total = 0
# for number in numbers:
#     total = total + number
# print(f"Sum of numbers in list: {total}")
# 3
# numbers = []
# while True:
#     input_number = int(input("Enter a number (0 to finish): "))
#     if input_number == 0:
#         break
#     numbers.append(input_number)
# total = 0
# for number in numbers:
#     total = total + number
# print(f"Sum of numbers in list: {total}")

# Bai 4
# 1
# numbers = [5,1,8,92,7,30]
# print("Even numbers: ")
# for number in numbers:
#     if number % 2 ==0:
#         print(number)
# 2
# numbers = []
# while True:
#     input_number = int(input("Enter a number (0 to finish): "))
#     if input_number == 0:
#         break
#     numbers.append(input_number)
# total = 0
# print("Even numbers: ")
# for number in numbers:
#     if number % 2 ==0:
#         print(number)

# Bai 5
# 1
# quan= ["BD","BDL","CG","ĐĐ","HBT"]
# danso = [247100,333300,266800,420900,318000]
# 2
# max_pop = danso[0]
# min_pop = danso[0]
# max_index =0
# min_index = 0
# for i in range(len(danso)):
#     if danso[i] > max_pop:
#         max_pop = danso[i]
#         max_index = i
#     if danso[i] < min_pop:
#         min_pop = danso[i]
#         min_index = i
# print("Indices of:")
# print(f"- Most populated dist.: {max_index}")
# print(f"- Least populated dist.: {min_index}")
# 3
# print("Names of:")
# print(f"- Most populated dist.: {danso[max_index]}")
# print(f"- Least populated dist.: {danso[min_index]}")

# Bài 6
# 1
# quan= ["BD","BDL","CG","ĐĐ","HBT"]
# danso = [247100,333300,266800,420900,318000]
# dientich = [9.224,43.35,12.04,9.96,10.09]
# densities = []
# for i in range(len(danso)):
#     density = danso[i] / dientich[i]
#     densities.append(density)
# print("Popluation density of:")
# for i in range(len(quan)):
#     print(f"- {quan[i]}: {densities[i]}")
# 2
# avg_density = sum(densities) / len(densities)
# print(f"Average population density: {avg_density}")

# Bài 7
# 1
# high_scores = [78,56,67]
# # 2
# print("High scores:")
# for i in range(len(high_scores)):
#     print(i + 1, ".", high_scores[i])
# # 3
# new_score = int(input("Input new score: "))
# high_scores.append(new_score)
# for i in range(len(high_scores)):
#     print(i + 1, ".", high_scores[i])

# Bài 8
# 1
# high_scores = [78,56,67]
# new_score = int(input("Input new score: "))
# high_scores.append(new_score)
# high_scores.sort(reverse=True)
# print("High scores:")
# for i in range(len(high_scores)):
#     print(i + 1, ".", high_scores[i])
# 2
# high_scores = [78,70,67,56,45]
# new_score = int(input("Input new score: "))
# high_scores.append(new_score)
# high_scores.sort(reverse=True)
# top5 = high_scores[:5]
# print("High scores:")
# for i in range(len(top5)):
#     print(i + 1, ".", high_scores[i])