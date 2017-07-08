# coding:utf-8
import collections
'''
class Cpu(object):

    def __init__(self, xinhao='', num=0):
        self.xinhao = xinhao
        self.num = num
        #self.dict1 = {}
'''

Cpu = collections.namedtuple('Cpu', ['xinhao', 'num'])

        
class Computer(object):

    def __init__(self):
        #self.cpu = Cpu(xinhao='', num=0)
        self.dict1 = {}

    def add_cpu(self, name, amount=1):
        if name not in self.dict1:
            self.dict1[name] = amount
        else:
            self.dict1[name] += amount
        return self.dict1


computer = Computer()
computer.add_cpu('inter', 4) 
computer.add_cpu('inter', 5)
computer.add_cpu('amd', 4) 
print computer.dict11