#coding:utf-8
import math

class Point_1(object):
    '''
    以元组对的形式返回坐标
    求两点间的长度
    求斜率:k=tanα=（y2-y1）/（x2-x1）
    特殊情况：直线与X轴垂直则K不存在返回None,直线与X轴平行则K等于0
    '''
    def __init__(self,x=0,y=0,x1=0,y1=0):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1

    def __str__(self):
        return '((%d,%d),(%d,%d))'%(self.x, self.y, self.x1, self.y1)

    def length(self):
        return math.sqrt((self.x-self.x1)**2 + (self.y-self.y1)**2)

    def slope(self):
        if self.x1-self.x == 0:
            return None
        else:
            return float(self.y1-self.y)/(self.x1-self.x)

    __repr__ = __str__

if __name__ == '__main__':
    l = Point_1(1,2,3,4)
    print '两个坐标点为:',l
    print '直线长度为:%s'%l.length()
    print '直线斜率为:%s'%l.slope()




