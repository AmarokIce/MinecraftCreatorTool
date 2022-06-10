# -- coding: utf-8 --
# By someoneice

import os
import pprint
import time
from MinecraftTool.GetJSONHelper import GetJSONHelper
from MinecraftTool.GetReport import GetReport
from MinecraftTool.TickHelper import TickHelper
from MinecraftTool.UnicodeHelper import UnicodeHelper

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
            times = input('请输入时间数据')
            ticks = int(input('请输入刻度数据'))
            if times == 'exit':
                break
        except:
            print('发现无效的数据！')
        else:
            classTick = TickHelper(ticks, times)
            classTick.TimesHelper()

def classUnicode():
    while True:
        getString = input('请输入待转换文字')

        classUnicode = UnicodeHelper(getString)
        classUnicode.unicodeMode()

def CommandMune(Command):
    CommandTable = {
        'json':classJson,
        'report':classReport,
        'tick':classTick,
        'unicode':classUnicode
    }
    
    CommandTable[Command]()

HelpTable = {
    'json':'进入导出model Item json模式，用于导出模组model中Item Json。',
    'report':'进入错误报告过滤模式，挑出重点。',
    'tick':'进入Tick转换模式。',
    'unicode':'进入中文转Unicode字符模式。'
}


#* Start Main: Minecraft Creator Tool Pockage #
if __name__ == "__main__":
    while True:
        Command = input('如果你需要帮助，请输入help')
        if Command == 'help':
            pprint.pprint(HelpTable)
        elif Command == 'exit':
            os.exit(0)
        else:
            try:
                CommandMune(Command)
            except:
                print('如果你需要帮助，请输入help ； 如果你希望退出，请输入exit。')
        time.sleep(1)