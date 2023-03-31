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

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix[1][2])
# for row in matrix:
#     for item in row:
#         print(item)

# numbers = [4, 2, 1, 3, 5, 8, 5]
# numbers.insert(0, 9)    # 插入元素到列表0下标位置
# # numbers.remove(8)  # 删除指定值
# # numbers.clear()  # 清除列表内全部数据
# # numbers.pop()  # 直接调用清除列表最后一个元素
# print(numbers)
# print(numbers.index(8))  # 返回列表元素的索引
# print(10 in numbers)    # print检查10是否在列表内
# print(numbers.count(5))  # count统计列表里元素个数
# numbers.sort()  # 将列表内元素升序排序
# print(numbers)
# numbers.reverse()  # 将列表内元素降序排序
# print(numbers)
# numbers2 = numbers.copy()   # 复制列表
# numbers.append(11)
# print(numbers, numbers2)

# numbers = [2, 2, 4, 6, 3, 4, 6, 1]
# uniques = []
# for number in numbers:
#     if number not in uniques:   # 去重添加到列表里
#         uniques.append(number)
# print(uniques)

# numbers = (1, 2, 3)
# print(numbers[0])

# coordinates = (1, 2, 3)
# x, y, z = coordinates   # python的解压缩
# print(x)

# customer = {
#     "name": "ToddCombs",
#     "age": 37,
#     "is_verified": True
# }
# print(customer.get("name"))
# print(customer.get("birthdate"))
# print(customer.get("birthdate", "Jan 9 1986"))  # 如果字典里没有该字段，可以临时指定一个

# phone = input("Phone: ")
# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# }
# output = ""
# for ch in phone:
#     output += digits_mapping.get(ch, "!") + " "  # 如果输入的内容字典内没有键值，则用！替代
# print(output)

# def emoji_converter(message):
#     """
#     emoji转换器
#     :param message:
#     :return:
#     """
#     words = message.split(" ")  # 以空格分割
#     emojis = {
#         ":)": "😊",   # win键+">"键可以调出系统自带的emoji表情！
#         ":(": "😒"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
# message = input("> ")
# print(emoji_converter(message))

# def hello_user(first_name, last_name):
#     print(f"Hi {first_name} {last_name}!\nWelcome aboard")
# hello_user(first_name="Todd", last_name="Combs")

# def square(number):
#     """
#     练习
#     :param number:
#     :return:如果不写return，则默认返回none
#     """
#     return number * number  # 如果不写return，则默认返回none
# res = square(3)
# print(res)

# 错误处理
# try:
#     age = int(input('Age: '))
#     income = 20000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print('Age cannot be 0.')
# except ValueError:
#     print('Invalid value')

# class Point:
#     def __init__(self, x, y):
#         """
#         构造函数
#         :param x:
#         :param y:
#         """
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
# # point1 = Point()    # 类的实例化
# # point1.x = 10   # 设置实例属性
# # point1.y = 20
# # print(point1.x)  # 封装过程
# # point1.draw()
# # point2 = Point()
# # print(point2.x)  # 每个实例是独立的，point2没有封装x属性，因此会报错
# point = Point(10, 20)
# point.x = 11
# print(point.x)

class Persons:

    def __init__(self, name):
        self.name = name    # 构造函数继承

    def talk(self):
        print(f"Hi! I am {self.name}")

todd = Persons("Todd Combs")    # 传参给类的构造函数
todd.talk()