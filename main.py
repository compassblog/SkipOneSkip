# -*- coding: utf-8 -*-
__author__ = 'GitHung'
__date__ = '2018/6/27 14:16'

from operation import Operation
from algorithm import Algorithm
import random
import time
from draw import Draw


# 测试寻找关键坐标
def test_find_point():
    op = Operation()
    im = op.screen_cap()
    algorithm = Algorithm()
    start_x, start_y, end_x, end_y = algorithm.find_point(im)
    print("start_point:", start_x, start_y)
    print("end_point:", end_x, end_y)

    start_point = (start_x, start_y)
    end_point = (end_x, end_y)
    distance = algorithm.euclidean_distance(start_point, end_point)
    print("distance = %f" % distance)

def test_jump():
    algorithm = Algorithm()
    op = Operation()
    im = op.screen_cap()
    start_x, start_y, end_x, end_y = algorithm.find_point(im)
    start_point = (start_x, start_y)
    end_point = (end_x, end_y)
    distance = algorithm.euclidean_distance(start_point, end_point)
    press_time = algorithm.distance_to_time(distance)
    op.jump(start_point, end_point, press_time)

print('hello world!')
while True:
    rand = 0.5 + random.random()
    test_jump()
    time.sleep(rand)