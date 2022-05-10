# 一段pdf文件转换成图片的脚本，存储路径稍作修改，需要用到pdf2image 以及poppler-0.68.0
# 原帖地址http://www.51testing.com/html/42/n-4479042.html
import pathlib
import cv2
from math import *
import numpy as np
import detect
import recognize
output_dir = pathlib.Path(r"C:\Users\admin\PycharmProjects\Unit_Test\demo\pdf")
image = cv2.imread(f"{output_dir}/image17.png")
size_reshaped = (int(image.shape[1]), int(image.shape[0]))
image = cv2.resize(image, size_reshaped)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

filename = f"{output_dir}/image17.txt"
with open(filename, r"C:\Users\admin\PycharmProjects\Unit_Test\demo\pdf") as text:
    for line in text.readlines():
        print(line.strip("\n"))