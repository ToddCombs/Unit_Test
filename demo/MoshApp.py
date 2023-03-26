# Mosh的练习题
# full_name = "John Smith"
# age = 20
# is_new = True
# name = input("What is your name? ")
# favourite = input("What is your favourite color?")
# print('Hi ' + name + ', so you favourite color is ' + favourite)

# birth_year = input('Birth year: ')
# age = 2023 - int(birth_year)
# print(age)

# weight_lbs = input('you weight: ')
# weight_kg = float(weight_lbs) * 0.45
# print('the weight is ' + str(weight_kg))

# first = 'Todd'
# last = 'Combs'
# msg = f'[{first}] [{last}] is a python coder.'
# print(msg)

# course = 'python for Beginners'
# print(course.upper())   # 大写转换
# print(course.lower())   # 小写转换
# print(course.title())   # 首字母大写
# print(course.find('for'))   # 查找函数
# print(course.replace('for', 'of'))  # 替换
# print('python' in course)  # 判断字符串是否存在

# print(10 / 3)   # 浮点数结果
# print(10 // 3)  # 整数结果
# print(10 % 3)   # 返回除法取余数
# print(10 ** 3)  # 10的3次方
# x = 10
# x += 2          # 赋值运算，自身+值
# print(x)
# x -= 4          # 赋值运算，自身-值
# print(x)
# y = (2 + 3) * 10 -3
# print("y =", y)

# import math
# x = 2.9
# y = -2.9
# # print(round(x))  # 四舍五入函数round
# # print(abs(y))   # 绝对值函数abs
# print(math.ceil(2.9))   # 向上取整数ceil
# print(math.floor(2.9))  # 向下取整floor

# is_hot = False
# is_cold = False
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
# print("Enjoy your day")
# price = 1000000
# has_good_credit = True
# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"Down payment: ${down_payment}")
#
# has_high_income = False
# has_good_credit = True
# has_criminal_record = False
# # if has_high_income or has_good_credit:
# if has_good_credit and not has_criminal_record:
#     print("Eligible for loan")

# temperature = 30
# if temperature > 30:
#     print("It's a hot day")
# else:
#     print("It's not a hot day")
#
# name = "Todd Combs"
# if len(name) < 3:
#     print("Name must be at least 3 characters.")
# elif len(name) > 50:
#     print("Name must be a maximum of 50 characters.")
# else:
#     print("Name looks good!")

# weight = int(input('Weight: '))
# unit = input('(L)bs or (K)g: ')
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"You are {converted} kilos")
# else:
#     converted = weight / 0.45
#     print(f"You are {converted} pounds")
# i = 1
# while i <= 5:
#     print('*' * i)
#     i += 1
# print("Done")

# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == secret_number:
#         print("You won!")
#         break
# else:
#     print("Sorry, You failed!")

# command = ""
# started = False
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:  # 如果started是假则说明车辆已启动，打印车辆已启动
#             print("Car is already started!")
#         else:   # 否则started修改为真值（启动状态）并打印车辆启动
#             started = True
#             print("Car started...")
#     elif command == "stop":
#         if not started:
#             print("Car is already stopped!")
#         else:
#             started = False
#             print("Car stopped.")
#     elif command == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("Sorry, I don't understand that.")

# for item in range(5, 10, 2):    # 第三个函数是步长
#     print(item)
#
# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price  # 列表内元素相加
# print(f"Total: {total}")
#
# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')

# numbers = [5, 2, 5, 2, 2]
# for number in numbers:
#     # print(number * '*')
#     output = ''
#     for count in range(number):
#         output += 'x'
#     print(output)

# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# names[0] = 'Joh'
# print(names)

# 冒泡排序
# numbers = [3, 6, 10, 2, 8, 4]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])
for row in matrix:
    for item in row:
        print(item)