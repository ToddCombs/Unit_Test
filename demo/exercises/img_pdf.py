# python合成多张图片转换成PDF格式的小工具(希望有的人永远也用不上)
# 原帖：https://zhuanlan.zhihu.com/p/483425913
from PIL import Image
import os

def combine_imgs_pdf(folder_path, pdf_file_path):
    """
    转换图片为pdf格式
    :param folder_path(str): 源文件夹
    :param pdf_file_path(str): 输出路径
    :return:
    """
    files = os.listdir(folder_path)
    png_files = []
    sources = []
    for file in files:
        if 'png' in file or 'jpg' in file:
            png_files.append(folder_path + file)
    png_files.sort()
    output = Image.open(png_files[0])
    png_files.pop(0)
    for file in png_files:
        png_files = Image.open(file)
        if png_files.mode == "RGB":
            png_files = png_files.convert("RGB")
        sources.append(png_files)
    output.save(pdf_file_path, "pdf", save_all=True, append_images=sources)

if __name__ == "__main__":
    folder = r"C:\Users\Administrator\Pictures\转账记录\\"
    pdfFile = r"C:\Users\Administrator\Pictures\转账记录\转账记录.pdf"
    combine_imgs_pdf(folder, pdfFile)