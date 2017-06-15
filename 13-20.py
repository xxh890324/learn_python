# coding:utf-8
class Time60(object):
    '''
    修改并优化Time60,支持60进制运算
    支持以下输入格式：
    1、Time(10,30)
    2、Time((10,30))
    3、Time('10:30')
    4、Time({'hr':10,'min':30})
    type()方法区分传入参数的类型，根据类型把hr和min取出来赋值给self.hr和self.min
    个人认为不需要实现__radd__方法。如果类Time60中没有__add__方法，这时我们应该覆盖__radd方法__
    '''
    
    def __init__(self, *hr_min):
        if type(hr_min[0]) is tuple:
            self.hr = hr_min[0][0]
            self.min = hr_min[0][1]
        elif type(hr_min[0]) is dict:
            self.hr = hr_min[0]['hr']
            self.min = hr_min[0]['min']
        elif type(hr_min[0]) is str:
            self.hr = int(hr_min[0].split(':')[0])
            self.min = int(hr_min[0].split(':')[1])
        elif type(hr_min) is tuple:
            self.hr = hr_min[0]
            self.min = hr_min[1]
    
    def __str__(self):
        return '%02d:%02d' % (self.hr, self.min)

    def __repr__(self):
        return repr('%02d:%02d' % (self.hr, self.min))

    def __add__(self, other):
        hr = self.hr + other.hr
        min = self.min + other.min
        if hr >= 24:
            hr -= 24
        if min >= 60:
            min -= 60
            hr += 1
        return self.__class__(hr, min)

    def __iadd__(self, other):
        hr = self.hr + other.hr
        min = self.min + other.min
        if hr >= 24:
            hr -= 24
        if min >= 60:
            min -= 60
            hr += 1
        return self.__class__(hr, min)


t1 = Time60('12:10')
t2 = Time60((10, 56))
print '''t1 = Time60('12:10')
t2 = Time60((10, 56))
t1 + t2'''
print '结果为:', t1 + t2
t3 = Time60(10, 30)
t4 = Time60({'hr': 10, 'min': 30})
print '''t3 = Time60(10,30)
t4 = Time60({'hr':10,'min':30})
t3 += t4'''
t3 += t4
print 't3结果为:', t3
