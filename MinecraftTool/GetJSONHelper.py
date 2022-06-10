# -- coding: utf-8 --
# By someoneice

import os
import time
from tkinter.filedialog import askopenfilename

class GetJSONHelper:
    def __init__(self, modid):
        self.modid = modid

    def getJsonHelper(self):
        mod_path = os.path.dirname(os.path.abspath(__file__))
        
        input_path = os.path.join(mod_path, "inputJson")
        if os.path.exists(input_path):
          pass
        else:
          os.mkdir(input_path)

        while True:
          print('''
                [
                  "layer0",
                  "layer1",
                  "layer2",
                  ...
                  "layerN"
                ]
                ''')
          input('請將即將導入的內容按照上方演示格式填入json,按下Enter后选择向导将会出现。')
          try:
            self.filename = askopenfilename()

            with open(f'{self.filename}') as f:
                 Item = json.load(f)
          except:
            print("无效的检索！")
            time.sleep(1)
          else:
            print(Item)
            __getJson = input('請檢查即將輸入文件是否為上述格式，若沒有問題，請輸入yes或者y繼續。')
            if __getJson == 'yes' or __getJson == 'y':
                break

        __output_path = os.path.join(mod_path, "outputJson")
        print('即將輸出Json到' + __output_path)

        if os.path.exists(__output_path):
          pass
        else:
          os.mkdir(__output_path)

        for NameHelper in Item:
          Icon = '''
          {
            "parent": "item/generated",
            "textures": {
              "layer0": "%s:item/%s"
            }
          }
          '''%(self.modid, NameHelper)

          with open(__output_path+'/%s.json'%NameHelper, 'w') as json:
            json.write(Icon)

        print('完畢，正在退出狀態...')
        time.sleep(1)


if __name__ == '__main__':
  modid = input('请输入modid')
  classJson = GetJSONHelper(modid)
  classJson.getJsonHelper()