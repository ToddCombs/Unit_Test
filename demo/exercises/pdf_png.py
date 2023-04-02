# 一段pdf文件转换成图片的脚本，存储路径稍作修改，需要用到pdf2image 以及poppler-0.68.0
# 原帖地址http://www.51testing.com/html/42/n-4479042.html
from pdf2image import convert_from_path
from pdf2image.exceptions import (PDFInfoNotInstalledError,
                                  PDFPageCountError,
                                  PDFSyntaxError)
pdf_path = r"C:\Users\admin\PycharmProjects\Unit_Test\demo\zzjl\流水证明_2022051200085004002497545325320064174781.pdf"
images = convert_from_path(pdf_path)
for i, images in enumerate(images):
    fname = "image" + str(i) + ".png"
    images.save(r"C:\Users\admin\PycharmProjects\Unit_Test\demo\zzjl_img\{}".format(fname))