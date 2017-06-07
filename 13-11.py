#coding:utf-8
import shelve
s = shelve.open('abc.db',writeback=True)
s.clear()
print s
