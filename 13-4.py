# coding:utf-8
import shelve
from datetime import datetime

class User(object):
    '''
    用户注册
    '''
    def __init__(self, db_path='user.db'):
        '''
        默认数据库文件为user.db
        '''
        self.my_db = shelve.open(db_path)
        self.db_path = db_path

    def __del__(self):
        '''
        shelve.open方法在默认只有关闭了才会将改变写入文件
        所以在垃圾回收时调用close方法
        '''
        my_data = shelve.open(self.db_path)
        my_data.update(self.my_db)
        my_data.close()

    def my_input(self):
        '''
        多次用到input用户名密码
        这里单独写成方法供其他方法调用
        '''
        username = raw_input('please input your username:')
        password = raw_input('please input your password:')
        return (username, password)

    def login(self, username, password):
        '''
        登录方法,登录时会记录登录时间
        '''
        if self.my_db[username][0] == password:
            self.my_db[username][1] = datetime.now()
            print 'login success'
            return True
        else:
            print 'login failed'
            return False

    def adduser(self, username, password):
        '''
        添加用户方法
        '''
        if self.my_db.has_key(username):
            print 'username is existed'
            return False
        else:
            self.my_db[username] = [password, datetime.now()]
            print 'add user success'
            return True

    def showusers(self, username):
        '''
        显示用户上次登录时间
        '''
        for user in self.my_db:
            print 'user:%s,last login time:%s' % (username, self.my_db[username][1])
        
    def main(self):
        pr = '''
        (N)ew User Login
        (E)xisting User Login
        (Q)uit
        Enter choice:
        '''
        while True:
            try:
                choice = raw_input(pr).strip().lower()
            except (EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'
            print '\nYou picked:[%s]' % choice
            if choice not in 'neq':
                print 'Invalid option,try again'
            else:
                if choice == 'n':
                    userlist = self.my_input()
                    self.adduser(userlist[0], userlist[1])
                    break
                if choice == 'e':
                    userlist = self.my_input()
                    self.login(userlist[0], userlist[1])
                    self.showusers(userlist[0])
                    break
        

if __name__ == '__main__':
    s = User()
    s.main()
