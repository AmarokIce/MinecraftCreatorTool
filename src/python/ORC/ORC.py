from tkinter.filedialog import askdirectory, askopenfilename
import pytesseract
import opencc
from PIL import Image


def getFile():
    log = askopenfilename(title="Select Log", filetypes=(("Log", "*.png"),))
    
    im = Image.open(log)
    string = pytesseract.image_to_string(im, lang='chi_tra')
    
    str(string)
    print
    print(string)
    return string

def ccFile(string):
    cc = opencc.OpenCC('t2s')
    string = cc.convert(string)
    str(string)
    return string

def writeFile(string):
    WriteFile = askdirectory(title = 'Selech FilePockage')
    with open(WriteFile+ "\\output.txt", "w", encoding="big5") as file:
        file.write(string)
    print('Done!')
    input('')

if __name__ == "__main__":
    string = getFile()
    while True:
        print('请确认结果。是否继续？（Yes or No')
        getFileInPut = input('')
        if getFileInPut == 'Yes' or getFileInPut == 'yes' or getFileInPut == 'y':
            string = ccFile(string)
            writeFile(string)
        
        elif getFileInPut == 'No' or getFileInPut == 'no' or getFileInPut == 'n':
            break
        
        else:
            pass
    print('已经完成执行。')
