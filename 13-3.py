#coding:utf-8
import locale

class MoneyFmt(object):
    '''
    货币格式化
    '''

    def __init__(self,cash,curr='$',choose='-'):
        self.cash = float(cash)
        self.curr = curr
        self.choose = choose

    def __nonzero__(self):
        if self.cash == 0:
            return False
        else:
            return True

    def __repr__(self):
        return repr(self.cash)

    def __str__(self):
        locale.setlocale(locale.LC_ALL, '')
        val = ''
        if self.cash < 0:
            if self.choose == '-':
                val = '-' + self.curr + locale.format('%.2f',0-self.cash,1)
            if self.choose == '<>':
                val = '<' + self.curr + locale.format('%.2f',0-self.cash,1) + '>'
        if self.cash > 0:
            val = self.curr + locale.format('%.2f',self.cash,1)
        return val

    def update(self,values):
        self.cash = values
        return self.cash

a = MoneyFmt(0,'$','<>')
print a
