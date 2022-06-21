# -- coding: utf-8 --
# By someoneice

import os
import time
import requests
import zipfile
import shutil
from update.MoveZIPFile import MoveZIPFile

class UpdateFile:
    def __init__(self, url):
        self.url = url
        
        self.projectFilePath = os.path.abspath(os.path.join(os.path.dirname(__file__),'../../..'))
        self.filePath = os.path.abspath(os.path.join(os.path.dirname(__file__),))
        
    def download(self):
        req = requests.get(self.url)
        self.filename = self.url.split('/')[-1]
        if req.status_code != 200:
            print('下载异常')
            return
        try:
            with open(self.filePath + '\\' + self.filename, 'wb') as f:
                f.write(req.content)
                print('下载成功')
        except:
            print('未知的错误，请检查网络。')
        
        self.filedir = (self.filePath + '\\' + self.filename)
    
    # Start Update MinecraftTools.
    def update(self):
        # Unzip the file.
        zip = zipfile.ZipFile(self.filedir)
        zip.extractall(self.projectFilePath)
        zip.close()
        time.sleep(1)
        print('已完成解压！')
        print('正在迁移主文件...')
        time.sleep(2)
        
        projectPockage = self.projectFilePath + '\\MinecraftCreatorTool-master'
        MainProject = projectPockage + '\\src\\python\\Main.py'
        MoveProject = projectPockage + '\\src\\python\\core\\update\\MoveZIPFile.py'
        OldMainProject = self.projectFilePath + '\\src\\python\\Main.py'
        OldMoveProject = self.projectFilePath + '\\src\\python\\core\\update\\MoveZIPFile.py'
        
        MineSrc = os.path.join(projectPockage, MainProject)
        MoveSrc = os.path.join(projectPockage, MoveProject)
        newMineSrc = os.path.join(self.projectFilePath, OldMainProject)
        newMoveSrc = os.path.join(self.projectFilePath, OldMoveProject)
        
        shutil.move(MineSrc, newMineSrc)
        shutil.move(MoveSrc, newMoveSrc)

        print('完成！准备迁移全部文件...')
        
        
        MoveClass = MoveZIPFile()
        MoveClass.movefile()


if __name__ == '__main__':
    url = str(input())
    updateClass = UpdateFile(url)
    updateClass.download()
    updateClass.update()
    
    MoveClass = MoveZIPFile()
    MoveClass.movefile()