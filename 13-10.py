# coding:utf-8

class Fifo_lifo(object):
    

    '''
    同时具备FIFO和LIFO操作行为的数据结构
    实现以下方法：
    1、shift():返回并删除列表中第一个元素
    2、unshift():在列表的头部压入一个新元素
    3、pushit():列表尾部加上一个新元素
    4、popit():返回并删除列表中最后一个元素
    '''

    def __init__(self, stack=[]):
        self.stack = stack

    def shift(self):
        '''
        删除列表头元素，并返回它
        '''
        return self.stack.pop(0)

    def unshift(self):
        '''
        列表头部压入一个新元素
        '''
        return self.stack.insert(0, raw_input('please input a str:'))

    def pushit(self):
        '''
        列表尾部加入一个新元素
        '''
        return self.stack.append(raw_input('please input a str:'))

    def popit(self):
        '''
        返回并删除最后一个元素
        '''
        return self.stack.pop()

    def viewstack(self):
        return self.stack

    CMDs = {'s': shift, 'u': unshift, 'p': pushit, 'o': popit, 'v': viewstack}

    def main(self):
        pr = '''
        (s)hift
        (u)nhift
        (p)ushit
        p(o)pit
        (v)iewstack
        (q)uit
        enter choice:'''
        while True:
            while True:
                try:
                    choice = raw_input(pr).strip().lower()
                except (EOFError, KeyboardInterrupt, IndexError):
                    choice = 'q'
                print '\nYou picked:[%s]' % choice
                if choice not in 'supovq':
                    print 'Invalid option,try again'
                else:
                    break
            if choice == 'q':
                break
            else:
                print self.CMDs[choice](self)


if __name__ == '__main__':
    s = Fifo_lifo([1, 3, 5, 7, 9])
    s.main()