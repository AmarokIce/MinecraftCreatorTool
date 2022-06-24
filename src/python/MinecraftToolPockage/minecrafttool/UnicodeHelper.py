# -- coding: utf-8 --
# By someoneice

class UnicodeHelper:
    def __init__(self, getString):
        self.getString = getString

    def unicodeMode(self):
        self.getString = self.getString.encode('unicode_escape')
        self.getString = str(self.getString).replace('\\\\', '\\')
        self.getString = self.getString.replace('b', '')
        print(self.getString)


if __name__ == "__main__":
    while True:
        getString = input('请输入待转换文字：')

        ClassUnicode = UnicodeHelper(getString)
        ClassUnicode.unicodeMode()
