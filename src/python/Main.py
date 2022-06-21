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
import json
import sys
sys.path.append('src\\python\\core')
sys.path.append('src\\python\\core\\update')


import os
import pprint
import time
import requests
from minecrafttool.GetJSONHelper import GetJSONHelper
from minecrafttool.GetReport import GetReport
from minecrafttool.TickHelper import TickHelper
from minecrafttool.UnicodeHelper import UnicodeHelper
from icon.GIFHelper import GIFHelper
from core.UpdateFile import UpdateFile

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

def classUpdate():
    projectFilePath = os.path.abspath(os.path.join(os.path.dirname(__file__),'../..'))
    api = 'https://api.github.com/repos/AmarokIce/MinecraftCreatorTool'
    download = 'https://github.com/AmarokIce/MinecraftCreatorTool/archive/refs/heads/master.zip'
    
    def getProjectUpdate():
        def getFileTimes():
            f = {}
            files = os.listdir(projectFilePath)

            for file in files:
                times = os.path.getmtime(projectFilePath + file)
                f[file] = times
            return f

        def getGitHubUpdate(oldUpdateTimes):
            info = requests.get(api).json()
            updateTimes = time.mktime(time.strptime(info['updated_at'], '%Y-%m-%dT%H:%M:%SZ'))
            if not oldUpdateTimes:
                oldUpdateTimes = info['updated_at']
            if updateTimes > oldUpdateTimes:
                return True
            else:
                return False
        
        getFileTimes =  getFileTimes()
        for i in getFileTimes:
            isOld = getGitHubUpdate(getFileTimes[i])
            if isOld:
                return True
    
    
    def askForUpdate():
        mirror = [
            '若不需要自动推送，可以在config.json中将AutoUpdate设为False.',
            '0: 不更新',
            '1: 通过github更新（保持最新）',
            '2: 通过gitcode更新（国内镜像，较快，但是不一定是最新）'
            # '3: 通过git从github拉取（需要拥有git环境）'
        ]
        pprint.pprint(mirror)
        while True:
            j = input('是否进行自动更新？')
            if j == '0':
                break
                
            elif j == '1':
                while True:
                    try:
                        url = download
                        classUpdate = UpdateFile(url)
                        classUpdate.download()
                        classUpdate.update()
                        classUpdate.moveFile()
                        
                    except:
                        i =  input('遇到问题，是否重新尝试？(yes/no')
                        if i == 'yes':
                            pass
                        elif i == 'no':
                            break
                        
                    else:
                        print('以完成更新，即将进入菜单。')
                        break
                break
            
            elif j == '2':
                while True:
                    try:
                        url = 'https://gitcode.net/qq_36258771/MinecraftCreatorTool/-/archive/master/MinecraftCreatorTool-master.zip'
                        classUpdate = UpdateFile(url)
                        classUpdate.download()
                        classUpdate.update()
                        classUpdate.moveFile()
                        
                        
                    except:
                        i =  input('遇到问题，是否重新尝试？(yes/no')
                        if i == 'yes':
                            pass
                        elif i == 'no':
                            break
                    else:
                        print('以完成更新，即将进入菜单。')
                        break
                break
                                
            elif j == '3':
                print('未完成！')
            
            else:
                print('输入0结束对话。')
    
    try:
        getGitHubUpdate = getProjectUpdate()
    except:
        print('无法连接Github或遇到了其他问题！')
        askForUpdate()
    else:
        if getGitHubUpdate != False:
            askForUpdate()

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
    ConfigText = {
    "Auto-Update" : "True"
}
    Text = str(ConfigText)
    Text = Text.replace('\'', '\"')
    
    Config = os.path.abspath(os.path.join(os.path.dirname(__file__),'config.json'))
    if os.path.exists(Config):
        pass
    else:
        with open(Config, 'w') as configWriter:
            configWriter.write(Text)
            time.sleep(0.5)
    
    with open(Config, 'r', encoding='utf-8') as j:
        ConfigText = json.load(j)
        time.sleep(0.5)
    
    if "Auto-Update" in ConfigText:
        if ConfigText['Auto-Update'] == "True":
            classUpdate()
    else:
        with open(Config, 'w') as configWriter:
            configWriter.write(Text)
            classUpdate()
    
    
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