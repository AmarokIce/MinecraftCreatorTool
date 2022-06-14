# -- coding: utf-8 --
# By someoneice

import os
from tkinter.filedialog import askopenfilename
from PIL import Image

class GIFHelper:
    mod_path = os.path.dirname(os.path.abspath(__file__))
    __output_path = os.path.join(mod_path, "//output//")
    Img = Image.open(askopenfilename())
    print(Img)
    Img_size = Img.size
    m, n = Img_size[0], Img_size[1]
    w, h = 16, 16
    x, y = 0, 0
    for i in range(n // 16):
        region = Img.crop((x, y, x+w, y+h))
        y += 16
        region.save(__output_path + str(i) + ".png")


if __name__ == '__main__':
    classGIF = GIFHelper()
    try:
        classGIF()
    except:
        print('未知的問題。')
    else:
        print('以輸出到路徑下output文件夾。')