#coding:utf-8

class Stack(object):
    '''
    堆栈先进后出
    pushit方法压入一个数据项
    popit方法删除一个数据项
    isempty方法判断stack是否为空，空返回1，非空返回0
    peek方法取出最顶端的数据项，不删除
    '''

    def __init__(self,stack = []):
        self.stack = stack

    def pushit(self):
        '''
        往stack中压入数据项
        '''
        self.stack.append(raw_input('输入新字符:').strip())

    def popit(self):
        '''
        删除一个数据项
        '''
        if hasattr(self.stack,'pop'):
            self.stack.pop()
        else:
            del self.stack[-1]
        return self.stack

    def isempty(self):
        if len(self.stack) == 0:
            a = 1
        else:
            a = 0
        return a

    def peek(self):
        return self.stack[-1]

    def viewstack(self):
        return self.stack
    CMDs = {'u':pushit,'o':popit,'p':peek,'v':viewstack}



def main():
    
    pr = '''
    p(u)sh
    p(o)p
    (p)eek
    (v)iew
    (q)uit

    enter choice:'''

    while True:
        while True:
            try:
                choice = raw_input(pr).strip().lower()
            except (EOFError,KeyboardInterrupt,IndexError):
                choice = 'q'
            print '\nYou picked:[%s]'%choice
            if choice not in 'uovq':
                print 'Invalid option,try again'
            else:
                break
            if choice == 'q':
                break
            s = Stack()
            CMDs[choice]()


if __name__ == '__main__':
    main()

        
