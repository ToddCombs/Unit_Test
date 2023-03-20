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

temperature = 30
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

name = "Todd Combs"
if len(name) < 3:
    print("Name must be at least 3 characters.")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters.")
else:
    print("Name looks good!")

