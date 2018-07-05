# -*- coding: utf-8 -*-
__author__ = 'GitHung'
__date__ = '2018/6/27 16:19'


class Algorithm:
    def __init__(self):
        pass

    def euclidean_distance(self, p1, p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5

    def find_point(self, im):
        piece_x = piece_y = 0
        board_x = board_y = 0
        w, h = im.size
        im_pixel = im.load()
        # 记录小人所有的点
        points = []
        # 记录y的最大值
        piece_y_max = 0
        for i in range(h//3, 2*h//3):
            for j in range(w):
                pixel = im_pixel[j, i]
                # print('i = ',i,',j = ',j,'pixel = ',pixel)
                if(50 < pixel[0] < 58 and 53 < pixel[1] < 60 and 95 < pixel[2] < 100):
                    if i > piece_y_max:
                        piece_y_max = i
                    points.append((j, i))
        # print('piece_y_max = ',piece_y_max)

        bottom_x = []
        for x,y in points:
            if y == piece_y_max:
                bottom_x.append(x)

        piece_x = sum(bottom_x) // len(bottom_x)
        # print('pixel = ',piece_x)
        piece_y = piece_y_max - 20


        points = []  # 获取目标格子的 x 值
        for i in range(h//3, 2*h//3):
            if len(points) > 0:
                break
            last_pixel = im_pixel[0, i]
            for j in range(w):
                pixel = im_pixel[j, i]
                # 把当前点与最左边的点比较 如果RGB差异比较大 则认为是目标点
                if (abs(pixel[0] - last_pixel[0])
                        + abs(pixel[1] - last_pixel[1])
                        + abs(pixel[2] - last_pixel[2]) > 10):
                    points.append((j, i))

        top_x = []
        for x, y in points:
            top_x.append(x)

        board_x = sum(top_x) // len(top_x)
        # print("board_x = %d" % (board_x,))

        # 2.2计算目标格式子y值
        # 屏幕中心的值
        center_x = w / 2 + 23  # x的偏差是12
        center_y = h / 2   # y的偏差是9
        # 格子高和宽的比例
        height_per_width = 130/226
        # 计算出目标格子的y值(需要转换成整数)
        if piece_x < board_x:
            board_y = int(center_y - height_per_width * (board_x - center_x))
        else:  # 从右往左跳
            board_y = int(center_y + height_per_width * (board_x - center_x))

        # print("board_y = %d" % (board_y,))

        return piece_x, piece_y, board_x, board_y

    def distance_to_time(self, distance):
        # 当0分的时候 距离为 261.222128 时间为730
        p = 726 / 540.1787  # 该算法后面待优化
        press_time = distance * p
        return press_time
