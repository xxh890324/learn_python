# coding:utf-8


class Item(object):
    '''
    Item类只包含两个属性，也可以用下面的方式声明
    Item = collections.namedtuple('Item', ['product', 'price'])
    '''
    def __init__(self, product, price, amount):
        self.product = product
        self.price = price
        self.amount = amount


class Cart(object):
    '''
    购物车类有添加商品、删除商品、显示商品方法
    '''
    def __init__(self, name):
        '''
        购物车具有名称属性
        采用字典方式存储商品数量和对应价格
        '''
        self.name = name
        self.cart_dict = {}
        self.total = 0
        self.item = Item(product='', price=0, amount=0)

    def add_item(self, name, price, amount=1):
        self.item.product = name
        if self.item.product not in self.cart_dict:
            self.cart_dict[self.item.product] = [amount, price]
        else:
            self.cart_dict[self.item.product][0] += amount

    def del_item(self, name, amount=1):
        self.item.product = name
        if self.item.product in self.cart_dict and self.cart_dict[self.item.product] >= amount:
            self.cart_dict[self.item.product][0] -= amount
        if self.cart_dict[self.item.product][0] == 0:
            self.cart_dict.pop(self.item.product)

    def show_item(self):
        print '购物车名称:%s' % self.name
        for i in self.cart_dict:
            print '商品：%s,数量:%d,单价:%f,小计:%f' % (i, self.cart_dict[i][0], self.cart_dict[i][1], self.cart_dict[i][0] * self.cart_dict[i][1])
            self.total += self.cart_dict[i][0] * self.cart_dict[i][1]


class User(object):
    def __init__(self, name, cart_name):
        '''
        用户名称属性，字典存储用户名下的购物车以及购物车金额
        '''
        self.name = name
        self.user_cart = {}
        self.cart = Cart(cart_name)

    def add_cart(self):
        self.user_cart[self.name] = [self.cart.name, self.cart.total]

    def del_crat(self, name):
        self.cart.name = name
        self.user_cart.pop(self.cart.name)

    def show_cart(self):
        for i in self.user_cart:
            print '姓名:%s,购物车名：%s,购物车金额:%f' % (i, self.user_cart[i][0], self.user_cart[i][1])


def main():
    user1 = User('xiaoming', 'c1')
    user1.cart.add_item('apple', 20, 2)
    user1.cart.add_item('book', 2, 3)
    user1.cart.show_item()
    user1.add_cart()
    user1.show_cart()
    print id(user1)

    user1 = User('xiaoming', 'c2')
    user1.cart.add_item('aa', 10, 4)
    user1.cart.add_item('bb', 100, 6)
    user1.cart.show_item()
    user1.add_cart()
    user1.show_cart()
    print id(user1)


if __name__ == '__main__':
    main()