# -- coding: utf-8 --
# By someoneice

import pprint
import time
from tkinter.filedialog import askopenfilename

__all__ = ['OutputError']

class GetReport:
    def __init__(self): #? 初始化数据
        self.thisLine = 0
        self.__getSonLine = 0
        self.filename = None
        self.__getReport = False
        self.__canSonPockage = True
        self.__getErrorMod = list()
        self.__getErrorSonPockage = list()
        self.__startCatchErrorMod = False
        self.__isGetErrorMod = False
        self.__isGetDescription = False
        self.__getDescriptionLine = 0
        
    def Description(self, getDescription):
        __ReportDescription = {
            'Description: Updating screen events':'显示更新事件遇到障碍：这个问题可能由于电脑显卡硬件问题，或尝试在地狱门附近打开背包类GUI导致无法刷写GUI渲染事件。',
            'Description: Exception in server tick loop':'服务器循环异常：当做了一些超出服务器预期的事件时可能会发生，如尝试加入客户端模组进入服务端，当然也可能是意外崩溃。',
            'Description: Ticking entity':'Tick下生物问题或Tick问题：通常需要通过错误行来判断问题。',
            'Description: Initializing game':'游戏加载时错误:若错误行中出现org.lwjgl.opengl.xxxxx，这是渲染问题，通过换显卡或者换电脑或者更新显卡驱动。同需要通过具体错误行判断问题。',
            'Description: Rendering item':'渲染生物/物品遇到问题，如果不是电脑显卡与驱动问题，那可能是生物出现问题。若无法解决优先尝试通过Forge内置的清理错误实体，移除Mod不是你的第一选择。',
            'Description: There was a severe problem during mod loading that has caused the game to fail':'加载模组时遇到严重问题：可能是模组有必要依赖缺失或者有模组冲突导致。通过移除Mod排查。'
        }
        
        return __ReportDescription[getDescription]
    
    def OpenErrorReport(self):
        self.filename=askopenfilename()

        with open(f'{self.filename}') as f:
            filedata = f.readlines()
            for line in filedata:
                time.sleep(0.05) #? 迭代缓冲
                
                self.__getDescriptionLine = self.__getDescriptionLine + 1
                if 'Description' in line:
                    line = line.replace('\n','')
                    __getDescription = line
                    self.__isGetDescription = True
                    print('发现错误描述!')
                    self.thisLine = self.__getDescriptionLine
                
                if self.__getDescriptionLine == self.thisLine + 2:
                    line = line.replace('\n','')
                    __getErrorPockage = line
                    time.sleep(1)
                
                if self.__canSonPockage == True:
                    if 'at' in line:
                        self.__getSonLine += 1
                        line = line.replace('\t','')
                        line = line.replace('\n','')
                        self.__getErrorSonPockage.append(line)
                        time.sleep(0.5)
                    
                    if self.__getSonLine >= 10:
                        self.__canSonPockage = False

                if ''U' = Unloaded' in line:
                    self.__startCatchErrorMod = True

                if  self.__startCatchErrorMod == True:
                    if 'UE' in line:
                        line = line.replace('\t','')
                        line = line.replace('\n','')
                        line = line.replace('UE','')
                        self.__getErrorMod.append(line)
                        self.__isGetErrorMod = True
                        print('发现问题模组!')
                        
                    if 'UCHIJE' in line:
                        line = line.replace('\t','')
                        line = line.replace('\n','')
                        line = line.replace('UCHIJE','')
                        self.__getErrorMod.append(line)
                        self.__isGetErrorMod = True
                        print('发现问题模组!')
                        
            
            #* 数据输出
            if self.__isGetDescription == True:
                getDescription = __getDescription
                getPockage = __getErrorPockage
                getSonPockage = self.__getErrorSonPockage
            else:
                getDescription = 'Not Find!' 
                
            if self.__isGetErrorMod == True:
                getErrorMod = self.__getErrorMod
            else:
                getErrorMod = 'Not Find!'
            self.__getReport = True
            
            return getDescription, getPockage, getSonPockage, getErrorMod
            
    def OutputError(self):
        
        getDescription, getPockage, getSonPockage, getErrorMod = self.OpenErrorReport()
        
        if self.__getReport == True:
            print('问题：')
            print(getDescription)
            print('')
            time.sleep(1)
            print('头包：')
            print(getPockage)
            print('')
            time.sleep(1)
            print('头包下10行内容')
            for i in getSonPockage:
                pprint.pprint(i)
                time.sleep(0.5)
            print('')
            time.sleep(1)
            print('可能存在问题的Mod：')
            pprint.pprint(getErrorMod)
            print('')
            time.sleep(1)
            print('参考：')
            print(self.Description(getDescription))


if __name__ == '__main__':
    start = GetReport()
    start.OutputError()
    input('按下Enter关闭窗口...')