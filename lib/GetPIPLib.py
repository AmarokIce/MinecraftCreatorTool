import os
import pprint


def get_pip_in_ver():
    os.system("pip install numpy")
    os.system("pip install pillow")
    os.system("pip install matplotlib")
    os.system("pip install opencv")


def get_pip_in_oth():
    os.system("pip install -i https://pypi.tuna.tsinghua.edu.cn/simple numpy")
    os.system("pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pillow")
    os.system("pip install -i https://pypi.tuna.tsinghua.edu.cn/simple matplotlib")
    os.system("pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv")


def debug():
    os.system("java -version")
    os.system('python -V')
    
    
def start():
    
    Lib = {
    1:get_pip_in_ver,
    2:get_pip_in_oth,
    3:debug
    }
    
    print('即将安装以下库：')
    pprint.pprint('''
                  Numpy : Python数据运算常用库
                  Pillow : Python图像处理常用库
                  MatplotLib : Python数据绘图库
                  OpenCV : Python优质视觉图像处理库
                  ''')
    print('如果你已经拥有这些库，运行这份文件什么也不会发生。')
    print('请选择使用官方源或者镜像源（国内较快）:')
    while True:
        pprint.pprint([
            '1.通过官方源下载'
            '2.通过镜像源下载'
        ])
        try:
            getLibChose = int(input(''))
            if getLibChose in {1, 2}:
                Lib[getLibChose]()
                break
            else:
                print('请输入1或2。')
        except:
            print('不是整数或未知的错误。')


#* Start *#
start()
input('按下回车确认结果。')