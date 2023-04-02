# 最简单的python冒泡排序
def bubble_sort(array):
    for i in range(1, len(array)):
        for j in range(0, len(array)-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


if __name__ == '__main__':
    array = [10, 17, 50, 22, 30, 7, 25, 45, 5, 15, 37, 20]
    print(bubble_sort(array))