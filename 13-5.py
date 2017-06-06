#coding:utf-8
class point(object):
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d,%d)'%(self.x,self.y)

a = point(1,6)
print a
