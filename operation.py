# -*- coding: utf-8 -*-
__author__ = 'GitHung'
__date__ = '2018/6/27 14:17'

import os
import datetime
from PIL import Image
import random


class Operation():
    def __init__(self):
        pass

    def screen_cap(self):
        filename = time = datetime.datetime.now().strftime('%H%M%S')+'.png'
        cmd = 'adb shell screencap -p /sdcard/' + filename
        os.system(cmd)
        cmd = 'adb pull /sdcard/' + filename + ' img/' + filename
        os.system(cmd)
        return Image.open('img/' + filename)

    def jump(self, src, dst, press_time):
        rand = 100 * (random.random() - 0.5)
        rand1 = 100 * (random.random() - 0.5)
        press_time = int(press_time)
        cmd = "adb shell input swipe %d %d %d %d %d" % (
            int(src[0]) + rand, int(src[1]) + rand1,
            int(src[0]) + rand, int(src[1]) + rand1,
            press_time
        )
        print(cmd)
        os.system(cmd)
