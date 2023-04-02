def find_max(numbers):
    """
    冒泡排序找到列表内最大值，MoshAPP相关
    :return: 返回最大值
    """
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum

