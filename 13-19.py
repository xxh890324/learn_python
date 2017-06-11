# coding:utf-8
'''
如果方法为keys，返回keys本身，则程序无穷递归下去
可以将方法名改掉，其他不变，则返回的就是父类的keys方法
'''
class SortedKeyDict(dict):
    def keys_son(self):
        return sorted(self.keys())


d = SortedKeyDict((('zheng-cai', 67), ('hui-jun', 48), ('xin-yi', 21)))
print 'By iterator:'.ljust(12), [key for key in d]
print 'By keys():'.ljust(12), d.keys()