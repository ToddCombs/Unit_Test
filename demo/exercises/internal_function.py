# 一些必须知道的python内置函数
# 原帖http://www.51testing.com/html/39/n-4478939.html

from functools import reduce


# reduce() 函数，会把迭代对象中的下一个元素作用在函数上做累计计算
def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


result = reduce(add, [1, 2, 3, 4])
print("结果：", result)


# 计算列表的乘积
def mul(a, b):
    return a * b


result_mul = reduce(mul, [1, 2, 3, 4])
print("结果：", result_mul)

# 匿名函数lambda计算乘积
result_mul_lambda = reduce(lambda a, b: a * b, [1, 2, 3, 4])
print("匿名函数lambda计算乘积结果：", result_mul_lambda)

# operator函数计算乘积
result_operator_mul = reduce(mul, [1, 2, 3, 4])
print("operator计算乘积结果：", result_operator_mul)

# split()将字符串分割成列表
words = "python is the best programming language"
wordswords = words.split(" ")
print(wordswords)

# enumerate()枚举，一般出现在需要获取列表下标位置时
# index = 0
# for w in wordswords:
#     print(index, w)
#     index += 1
for index, w in enumerate(wordswords):
    print(index, w)

# map() 函数是与reduce函数对应的，用于把一个列表通过函数处理，映射成一个新的列表
# 例如给列表的每个元素做平方，将列表元素转换成字符串，得到一个新的列表。
result_map = map(lambda x: str(x), [1, 2, 3, 4])
print(list(result_map))
result_map = map(lambda x: x * x, [1, 2, 3, 4])
print(list(result_map))


# map函数可接受多个列表参数，使多列表合并为一个列表成为可能。如将A,B列表同位置的数相加得到新列表
def merge(x, y):
    return x + y


result_merge = map(merge, [1, 2, 3], [3, 2, 1])
print(list(result_merge))
