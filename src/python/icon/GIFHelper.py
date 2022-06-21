# -- coding: utf-8 --
# By someoneice

import os
from tkinter.filedialog import askopenfilename
from PIL import Image

class GIFHelper:
    def __init__(self):
        self.mod_path = os.path.dirname(os.path.abspath(__file__))
        self.output_path = os.path.join(self.mod_path, "output\\")

        if os.path.exists(self.output_path):
            pass
        else:
            os.mkdir(self.output_path)
            
    def Start(self):
        Img = Image.open(askopenfilename(title="Select PNG file", filetypes=(("PNG files", "*.png"),)))
        print(Img)
        Img_size = Img.size
        m, n = Img_size[0], Img_size[1]
        w, h = 16, 16
        x, y = 0, 0
        for i in range(n // 16):
            getImg = Img.crop((x, y, x+w, y+h))
            y += 16
            getImg.save(self.output_path + str(i) + ".png")

if __name__ == '__main__':
    classGIF = GIFHelper()
    try:
        classGIF.Start()
    except:
        print('未知的問題。')
    else:
        print('以輸出到本文件夾下Output文件夾。')