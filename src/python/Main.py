# -- coding: utf-8 --
# By someoneice

'''
=== Pineapple license ===
I will provide all or part of the code, as long as you use it within the limits of the law, you can use these codes as you like.
You can get full access to this source code without paying any royalties, which will be permanent and irrevocable if you are granted this license. 
If you have made a copy of the Program with these code, you should include this license to keep the original code open source.
Of course this license doesn't used in court, just like you know that none of us want legal battles for these meaningless things, so I hope you will respect this brief license.
I do not want my code to be used for commercial purposes, including but not limited to paid downloads.
If you think my mod is good to learn something, if you like, invite me to a cup of pineapple juice.
If you do not follow this simple agreement and legal liability arises, this has nothing to do with me, please take responsibility for yourself.
If you're selling my source code or compiled code, I'll be very angry and accuse you smelling ugly.

If you are unable to accept a license other than those approved by the Open Source Initiative, you may use these codes using the AFL-3.0 license, instead of complying with this license.
If you choose to accept AFL-3.0, you may need to show in your README or somewhere else that is very convenient to see, you are using the AFL-3.0 license.

'''

import os
import pprint
import time
from minecrafttool.GetJSONHelper    import GetJSONHelper
from minecrafttool.GetReport        import GetReport
from minecrafttool.TickHelper       import TickHelper
from minecrafttool.UnicodeHelper    import UnicodeHelper
from icon.GIFHelper                 import GIFHelper

def classJson():
    while True:
        print('输入modid处输入exit可以退出模式')
        modid = ('请输入modid：')
        if modid == 'exit':
            break

        classJson = GetJSONHelper(modid)
        classJson.getJsonHelper()

def classReport():
    classReport = GetReport()
    classReport.OutputError()

def classTick():
    print('时间数据看表：')
    print('seconds:秒')
    print('min:分钟')
    print('hour:小时')
    print('day:天')
    print('exit:退出程序')

    while True:
        try:
            times = input('请输入时间数据:')
            if times == 'exit':
                break

            ticks = int(input('请输入刻度数据:'))
        except:
            print('发现无效的数据！')
        else:
            classTick = TickHelper(ticks, times)
            classTick.TimesHelper()

def classUnicode():
    while True:
        getString = input('请输入待转换文字：')
        if getString == 'exit':
            break

        classUnicode = UnicodeHelper(getString)
        classUnicode.unicodeMode()

def classGIF():
    classGIFHelper = GIFHelper()
    classGIFHelper()

def CommandMune(Command):
    CommandTable = {
        'json': classJson,
        'report': classReport,
        'tick': classTick,
        'unicode': classUnicode,
        'gif' : classGIF
    }

    CommandTable[Command]()

HelpTable = {
    'json': '进入导出model Item json模式，用于导出模组model中Item Json。',
    'report': '进入错误报告过滤模式，挑出重点。',
    'tick': '进入Tick转换模式。',
    'unicode': '进入中文转Unicode字符模式。'
}


#* Start Main: Minecraft Creator Tool Pockage #
if __name__ == "__main__":
    while True:
        Command = input('如果你需要帮助，请输入help：')
        if Command == 'help':
            pprint.pprint(HelpTable)
        elif Command == 'exit':
            os._exit(0)
        else:
            try:
                CommandMune(Command)
            except:
                print('如果你需要帮助，请输入help ； 如果你希望退出，请输入exit。')
        time.sleep(1)