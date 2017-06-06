#coding:utf-8
import time

class My_date(object):

    def __init__(self,date=time.time()):
        self.date = date

    def update(self):
        return time.ctime(self.date)

    def display(self,date_type):
        types = {'MDY':'%m/%d/%y','MDYY':'%m/%d/%Y','DMY':'%d/%m/%y','DMYY':'%d/%m/%Y','MODYY':'%b %d,%Y'}
        if date_type in types:
            return time.strftime(types[date_type],time.localtime(self.date))
        else:
            return update()

if __name__ == '__main__':
    d1 = My_date()
    print '当前日期为：',d1.update()
    a = ['MDY','MDYY','DMY','DMYY','MODYY']
    for i in a:
        print i+'格式显示日期：'+d1.display(i)




