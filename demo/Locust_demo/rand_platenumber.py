import random
from icecream import ic


def rand_plateNumbers():
    '''
    生成随机车牌函数
    :return:
    '''
    char0 = '京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽赣粤青藏川宁琼'
    char1 = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
    char2 = '1234567890'

    id_1 = random.choice(char0)  # 车牌第一位
    id_2 = ''.join(random.sample(char1, 1))  # 车牌第二位

    while True:
        id_3 = ''.join(random.sample(char2, 5))
        v = id_3.isalpha()  # 所有字符都是字母时返回True
        if v == True:
            continue
        else:
            plateNumber = id_1 + id_2 + id_3
            break
    return plateNumber

ic(rand_plateNumbers())