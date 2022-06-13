# -- coding: utf-8 --
# By someoneice

class UnicodeHelper:
    def __init__(self, getString):
       self.getString = getString
       
    def unicodeMode(self):
        self.getStr = self.getStr.encode('unicode_escape')
        self.getStr = self.getStr.replace('\\\\','\\')
        print(self.getStr)


if __name__ == "__main__":
    while True:
        getString = input('请输入待转换文字：')
    
        ClassUnicode = UnicodeHelper(getString)
        ClassUnicode.unicodeMode()