# Phần 1
# 1
# products = {
#     "HP": 20,
#     "DELL": 50,
#     "MACBOOK": 12,
#     "ASUS": 30 
# }
# 2
# print(f"Available MACBOOKs: {products['MACBOOK']}")

# 3
# brand = input("Input a brand: ")
# print(f"Available {brand}s: {products[brand]}")

# Phần 2
# 1
# products = {
#     "HP": 20,
#     "DELL": 50,
#     "MACBOOK": 12,
#     "ASUS": 30,
# }
# products["TOSHIBA"] = 10
# print("Available products:")
# for product, value in products.items():
#     print(f"- {product}: {value}")

# 2
# brand = input("Input a brand: ")
# amount = input("Input amount: ")
# products[brand] = amount
# print("Available products:")
# for product, value in products.items():
#     print(f"- {product}: {value}")

# 3
# products["DELL"] = 60
# products["MACBOOK"] = 2
# print("Available products:")
# for product, value in products.items():
#     print(f"- {product}: {value}")

# 4
# total = sum(products.values())
# print(f"Total products: {total}")

# Phần 3
# 1
# prices = {
#     "HP": 600,
#     "DELL": 650,
#     "MACBOOK": 1200,
#     "ASUS": 400,
# }

# 2
# print(f"Price of ASUS: {prices['ASUS']}")

# 3
# brand = input("Input a brand: ")
# print(f"Price of {brand}: {prices[brand]}")

# Phần 4
# 1
# prices = {
#     "HP": 600,
#     "DELL": 650,
#     "MACBOOK": 1200,
#     "ASUS": 400,
# }
# total = prices["ASUS"] * 5
# print(f"Total price: {total}")

# 2
# brand = input("Input a brand: ")
# amountbuy = int(input("Input amount to buy: "))
# total = prices[brand] * amountbuy
# print(f"Total price: {total}")

# 3
# prices = {
#     "HP": 600,
#     "DELL": 650,
#     "MACBOOK": 1200,
#     "ASUS": 400,
# }
# products = {
#     "HP": 20,
#     "DELL": 50,
#     "MACBOOK": 12,
#     "ASUS": 30,
# }
# brand = input("Input a brand: ")
# amountbuy = int(input("Input amount to buy: "))
# total = prices[brand] * amountbuy
# products[brand] -= amountbuy
# print(f"Total price: {total}")
# for product, value in products.items():
#     print(f"- {product}: {value}")

# Phần 5
# 1
# products = {
#     "HP": 20,
#     "DELL": 50,
#     "MACBOOK": 12,
#     "ASUS": 30,
# }
# prices = {
#     "HP": 600,
#     "DELL": 650,
#     "MACBOOK": 1200,
#     "ASUS": 400,
# }
# print("Total value of available brands: ")
# for brand in products:
#     total = products[brand] * prices[brand]
#     print(f"- {brand}: {total}")

# 2
# products = {
#     "HP": 20,
#     "DELL": 50,
#     "MACBOOK": 12,
#     "ASUS": 30,
# }
# prices = {
#     "HP": 600,
#     "DELL": 650,
#     "MACBOOK": 1200,
#     "ASUS": 400,
# }
# total = 0
# for brand in products:
#     total += products[brand] * prices[brand]
# print(f"Total value of available items: {total}")

# Phần 6
# 1
# character = {
#     "Name": "Light",
#     "Age": 17,
#     "Strength": 8,
#     "Defense": 10,
#     "HP": 100,
#     "Backpack": ["Shield", "Bread Loaf"],
#     "Gold": 100,
#     "Level": 2 
# }

# 2
# character["Gold"] += 50
# print(f"Gold: {character["Gold"]}")

# 3
# character["Backpack"].append("FlintStone")
# print(f"Backpack: {character['Backpack']}")

# Phần 7
# 1
# skills = [
#     {"Name": "Tackle", "Minimum level": 1, "Damage": 5, "Hit rate": 0.3},
#     {"Name": "Quick Attack", "Minimum level": 2, "Damage": 3, "Hit rate": 0.5},
#     {"Name": "Strong Kick", "Minimum level": 4, "Damage": 9, "Hit rate": 0.2},
# ]
# 2
# for i in range(len(skills)):
#     print(f"Skill {i + 1}: {skills[i]["Name"]}")

# Phần 8
# 1
# skills = [
#     {"Name": "Tackle", "Minimum level": 1, "Damage": 5, "Hit rate": 0.3},
#     {"Name": "Quick Attack", "Minimum level": 2, "Damage": 3, "Hit rate": 0.5},
#     {"Name": "Strong Kick", "Minimum level": 4, "Damage": 9, "Hit rate": 0.2},
# ]
# level = 2

# for i in range(len(skills)):
#     print(f"Skill {i+1}: {skills[i]['Name']}")

# choice = int(input("Choose skill by number: "))

# skill = skills[choice - 1]

# print("You chose", skill["Name"])

# if level >= skill["Minimum level"]:
#     print("Damage:", skill["Damage"])
# else:
#     print("Cannot deploy. Required level", skill["Minimum level"])

# 2
# import random

# level = 2

# for i in range(len(skills)):
#     print(f"Skill {i+1}: {skills[i]['Name']}")

# choice = int(input("Choose skill by number: "))

# skill = skills[choice - 1]

# print("You chose", skill["Name"])

# if level >= skill["Minimum level"]:
#     if random.random() < skill["Hit rate"]:
#         print("Damage:", skill["Damage"])
#     else:
#         print("Missed.")
# else:
#     print("Cannot deploy. Required level", skill["Minimum level"])