# path = "C:\\Users\\Dell\\Downloads\\CSB42\\Day10\\names.txt"
# Bai 1
# with open(path, "w") as file:
#     file.write("Nikki Roysden\n")
#     file.write("Mervin Friedland\n")
#     file.write("Aron Wilkins\n")
#     file.close()

# Bai 2
# filename = input("Input file name: ")
# with open(path, "r") as file:
#     content = file.read()
#     print("File content:")
#     print(content)

# Bai 3
# path = "C:\\Users\\Dell\\Downloads\\CSB42\\Day10\\user-inputs.txt"
# print("Enter content:")
# lines = []
# while True:
#     line = input()
#     if line == '':
#         break
#     lines.append(line)
# with open(path, "w") as file:
#     for line in lines:
#         file.write(line + "\n")

# Bai 4
import datetime
path = "C:\\Users\\Dell\\Downloads\\CSB42\\Day10\\input-logs.txt"
with open(path, "r") as file:
    content_old = file.read()
    print("Enter input: ")