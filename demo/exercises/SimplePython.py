# 一些常用好用的python代码
# 来源：http://www.51testing.com/html/58/n-4478758.html
import random
import secrets
import sys
import time
from collections import Counter
from time import *

from iteration_utilities import deepflatten


def reversed_string():
    """Reversing a string using slicing 反转字符串"""
    my_string = "ABCDE"
    reversed_string = my_string[::-1]
    print(reversed_string)


reversed_string()


def name_string():
    """字符串首字母大写"""
    my_string = "my name is todd combs"
    new_string = my_string.title()
    print(new_string)


name_string()


def research_string():
    """查找字符串的唯一要素，去掉字符串中的重复字符"""
    my_string = "aavvccccddddeee"
    temp_set = set(my_string)
    new_string = ' '.join(temp_set)
    print(new_string)


research_string()


def printlist():
    """输出N次字符串或列表，直接使用*相乘"""
    n = 3
    my_string = "abcd"
    my_list = [1, 2, 3]
    print(my_string * n)
    print(my_list * n)

    # 一个有趣的用例是定义一个具有恒定值的列表，假设为零
    n = 4
    my_list = [0] * n


printlist()


def onebyone_list():
    """列表解析，对列表的每个元素进行操作"""
    original_list = [1, 2, 3, 4]
    new_list = [2 * x for x in original_list]
    print(new_list)


onebyone_list()


def change_string():
    """交换变量的值"""
    a = 1
    b = 2
    a, b = b, a
    print(a)
    print(b)


change_string()


def split_string():
    """使用split()方法拆分字符串"""
    string_one = "My name is Todd Combs"
    string_two = "sample/ string_two"
    print(string_one.split())
    print(string_two.split('/'))


split_string()


def join_string():
    """列表元素合并，将字符串列表整合成单个字符串"""
    list_of_string = ['My', 'name', 'is', 'Todd', 'Combs']
    print(','.join(list_of_string))


join_string()


def palindrome_string():
    """检查字符串是否是回文（反转后的文字）"""
    my_string = "abcba"
    if my_string == my_string[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")


palindrome_string()


def count_string():
    """统计列表元素中最常出现的元素"""
    my_list = [1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 4, 4]
    count = Counter(my_list)
    print(count)
    print(count[2])
    print(count.most_common(1))


count_string()


def anagrams():
    """查找两个字符串是否为anagrams，
    两个字符串的counter对象相等，则他们就是anagrams"""
    str_one, str_two, str_three = "acbde", "abced", "abcda"
    cnt_one, cnt_two, cnt_three = Counter(str_one), Counter(str_two), Counter(str_three)
    if cnt_one == cnt_two:
        print("1 and 2 is anagrams")
    if cnt_one == cnt_three:
        print("1 and 3 is anagrams")


anagrams()


def try_except():
    """使用try-except-else模块"""
    a, b = 1, 0
    try:
        print(a / b)
    except ZeroDivisionError:
        print("division by zero")
    else:
        print("no exceptions raised")
    finally:
        print("Run this always")


try_except()


def research_sort():
    """以下脚本使用列举来迭代列表中的值及其索引。原始脚本有误，已修正"""
    my_list = ["a, b, c, d, e"]
    for index, value in enumerate(my_list):
        print("{0}: {1}".format(index, value))


research_sort()


def check_memory():
    """以下脚本检查对象的内存使用"""
    num = 21
    print(sys.getsizeof(num))


check_memory()


def merge_dict():
    """合并两个字典 """
    dict_one = {"apple": 9, "banana": 6}
    dict_two = {"banana": 4, "orange": 8}
    combined_dict = {**dict_one, **dict_two}
    print(combined_dict)


merge_dict()


def count_time():
    """用time函数计算执行一段代码所需时间，代码有误"""
    start_time = time.time()
    a, b = 1, 2
    c = a + b
    end_time = time.time()
    time_taken_in_micro = (end_time - start_time) * (10 ** 6)
    print("Time taken in micro_seconds: {0}ms".format(time_taken_in_micro))


count_time()


def flatten(I):
    """有时候不确定列表嵌套的深度，又想要全部要素在单个平面列表中展示可以通过以下方式"""
    return [item for sublist in I for item in sublist]


I = [[1, 2, 3], [3]]
print(flatten(I))
I = [[1, 2, 3], [4, [5], [6, 7]], [8, [9, [10]]]]
print(list(deepflatten(I, depth=3)))


def random_samples():
    """列表取样，通过random软件库，从给定的列表中生成N个随机样本"""
    my_list = ['a', 'b', 'c', 'd', 'e']
    num_samples = 2
    samples = random.sample(my_list, num_samples)
    print(samples)


random_samples()


# 列表取样python3用法
def secure_random():
    """列表取样python3用法，需要secrets库"""
    secure_random = secrets.SystemRandom()
    my_list = ['a', 'b', 'c', 'd', 'e']
    num_samples = 3
    samples = secure_random.sample(my_list, num_samples)
    print(samples)


secure_random()


def change_num():
    """将一个整数转换为数字列表"""
    num = 123456
    list_of_digits = list(map(int, str(num)))
    print(list_of_digits)
    list_of_digits = [int(x) for x in str(num)]
    print(list_of_digits)


change_num()


def check_onlyOne():
    """检查唯一性"""

    def unique(i):
        if len(i) == len(set(i)):
            print("All elements are unique")
        else:
            print("List has duplicates")

    unique([1, 2, 3, 4])
    unique([1, 1, 3, 4])


check_onlyOne()

elapsed = (time.clock() - start)
print("Time used:", elapsed)
