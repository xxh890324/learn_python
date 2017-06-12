# coding:utf-8
class Item(object):
    def __init__(self, product, price):
        '''
        商品包含产品名称、单价属性
        '''
        self.product = product
        self.price = price

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

    def add_item(self, Item, amount=1):
        if Item.product not in self.cart_dict:
            self.cart_dict[Item.product] = [amount, Item.price]
        else:
            self.cart_dict[Item.product][0] += amount

    def del_item(self, Item, amount=1):
        if Item.product in self.cart_dict and self.cart_dict[Item.product] >= amount:
            self.cart_dict[Item.product][0] -= amount
        if self.cart_dict[Item.product][0] == 0:
            self.cart_dict.pop(Item.product)

    def show_item(self):
        print '购物车名称:%s' % self.name
        for i in self.cart_dict:
            print '商品：%s,数量:%d,单价:%d,小计:%f' % (i, self.cart_dict[i][0], self.cart_dict[i][1], self.cart_dict[i][0] * self.cart_dict[i][1])
            self.total += self.cart_dict[i][0] * self.cart_dict[i][1]

class User(object):
    def __init__(self, name):
        '''
        用户名称属性，字典存储用户名下的购物车以及购物车金额
        '''
        self.name = name
        self.user_cart = {}

    def add_cart(self, Cart):
        self.user_cart[Cart.name] = Cart.total

    def del_crat(self, Cart):
        self.user_cart.pop(Cart.name)

    def show_cart(self):
        print '%s名下有以下购物车:' % self.name
        for i in self.user_cart:
            print '购物车名：%s,购物车金额:%f' % (i, self.user_cart[i])


def main():
    item1 = Item('TV', 1000)
    item2 = Item('Phone', 2000)
    item3 = Item('Computer', 3000)
    c1 = Cart('cart1')
    c2 = Cart('cart2')
    c1.add_item(item1, 2)
    c1.add_item(item2, 3)
    c1.add_item(item3, 4)
    c2.add_item(item1, 10)
    c2.del_item(item1)
    c1.show_item()
    c2.show_item()
    u1 = User('xxh')
    u1.add_cart(c1)
    u1.add_cart(c2)
    u1.show_cart()

if __name__ == '__main__':
    main()