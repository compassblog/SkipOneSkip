# -*- coding: utf-8 -*-
__author__ = 'GitHung'
__date__ = '2018/6/27 16:10'

import matplotlib.pyplot as plt

import cv2

class Draw:
    def __init__(self):
        self.fig = plt.figure()

    def draw(self, filename, scale=1):
        img = cv2.imread(filename)
        print(type(img))
        # img = cv2.resize(img, (0,0), fx=scale, fy=scale)
        plt.imshow(img)
        plt.show()
