# -- coding: utf-8 --
# By someoneice

import time

class TickHelper:
    def __init__(self, ticks, times):
        self.tick = 0
        self.mins = 0
        self.hour = 0
        self.days = 0
        try:
            self.ticks = int(ticks)
            self.times = str(times)
        except:
            print("存在问题的数据。")

    def TimesHelper(self):
        self.tick = self.ticks * 20
        self.mins = self.tick * 60
        self.hour = self.mins * 60
        self.days = self.hour * 24

        getTimesHelper = {
            'seconds': self.tick,
            'min': self.mins,
            'hour': self.hour,
            'day': self.days
        }

        print(getTimesHelper[self.times])


if __name__ == '__main__':
    print('seconds:秒')
    print('min:分钟')
    print('hour:小时')
    print('day:天')
    print('exit:退出程序')

    while True:
        times = input('请输入时间数据')
        ticks = int(input('请输入刻度数据'))
        ClassTickHelper = TickHelper(ticks, times)
        ClassTickHelper.TimesHelper()
        time.sleep(1)