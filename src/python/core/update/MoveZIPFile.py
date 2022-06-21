# -- coding: utf-8 --
# By someoneice

import os
import shutil
import time


class MoveZIPFile:
    def __init__(self):
        self.projectFilePath = os.path.abspath(os.path.join(os.path.dirname(__file__),'../../../..'))
        self.zipPath = self.projectFilePath + '\\src\python\core\MinecraftCreatorTool-master.zip'
    
    def movefile(self):
        projectPockage = self.projectFilePath + '\\MinecraftCreatorTool-master'
        filelist = os.listdir(projectPockage)
        for file in filelist:
            oldSrc = os.path.join(projectPockage, file)
            newSrc = os.path.join(self.projectFilePath, file)
    
            shutil.move(oldSrc, newSrc)
            time.sleep(0.5)
        print('已经完成更新！准备删除多余文件...')
        os.remove(self.zipPath)
        shutil.rmtree(projectPockage)