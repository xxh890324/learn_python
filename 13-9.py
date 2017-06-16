#coding:utf-8

class Queue(object):
    '''
    队列，先进先出，支持一下两个方法：
    1、enqueue()列表的尾部加入一个新元素
    2、dequeue()列表头部取出一个元素，返回它并且把它从列表删除
    '''

    def __init__(self, queue = []):
        self.queue = queue

    def enqueue(self):
        '''
        列表尾部加入一个元素
        '''
        self.queue.append(raw_input('please input a str:'))
        return self.queue

    def dequeue(self):
        '''
        取出列表头一个元素，返回它并且把它从列表删除
        '''
        return self.queue.pop(0)

    def viewqueue(self):
        '''
        显示列表元素
        '''
        return self.queue

    CMDs = {'e': enqueue, 'd': dequeue, 'v': viewqueue}

    def main(self):
        pr = '''
        (e)nqueue
        (d)equeue
        (v)viewqueue
        (q)uit
        enter choice:'''
        while True:
            while True:
                try:
                    choice = raw_input(pr).strip().lower()
                except (EOFError, KeyboardInterrupt, IndexError):
                    choice = 'q'
                print '\nYou picked:[%s]' % choice
                if choice not in 'edvq':
                    print 'Invalid option,try again'
                else:
                    break
            if choice == 'q':
                break
            else:
                print self.CMDs[choice](self)

if __name__ == '__main__':
    q = Queue([9, 8, 7, 6, 5])
    q.main()