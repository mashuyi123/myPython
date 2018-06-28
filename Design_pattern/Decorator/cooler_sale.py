#!/usr/bin/python
'''
题目：冷饮店有三种冷饮: 奶茶(4元) , 奶昔(5元) , 沙冰(6元) ,
另外: 加绿豆(1元) ,  加珍珠(2元) ,  加草莓(3元)    注 : 以后可能加蓝莓等
运用装饰者模式 , 模拟以下场景:
一杯奶茶 , 加入珍珠 , 再加入绿豆 , 计算出价格 
'''

 #基类
class cooler:
    description = "Unknown cooler"
 
    def get_description(self):
        return self.description
 
    def cost(self):
        pass
 #抽象方法
class  SnackDecorator(cooler):
    def get_description(self):
        pass
 
 #冷饮 奶茶
class MuilkTea(cooler):
    def __init__(self):
        self.description = "MuilkTea"
 
    def cost(self):
        return 4
 
 #冷饮 奶昔
class MuilkShake(cooler):
    def __init__(self):
        self.description = "MuilkShake"
 
    def cost(self):
        return 5
 
 #冷饮 沙冰
class Smoothie(cooler):
    def __init__(self):
        self.description = "Smoothie"
 
    def cost(self):
        return 6
 
 #配料 绿豆
class Gram(SnackDecorator):
    def __init__(self, cooler):
        self.cooler = cooler
 
    def get_description(self):
        return self.cooler.get_description() + " + Gram"
 
    def cost(self):
        return 1 + self.cooler.cost()
 
 #配料 珍珠
class Pearl(SnackDecorator):
    def __init__(self, cooler):
        self.cooler = cooler
 
    def get_description(self):
        return self.cooler.get_description() + " + Pearl"
 
    def cost(self):
        return 2 + self.cooler.cost()
 
 #配料 草莓
class Strawberry(SnackDecorator):
    def __init__(self, cooler):
        self.cooler = cooler
 
    def get_description(self):
        return self.cooler.get_description() + " + Strawberry"
 
    def cost(self):
        return 3 + self.cooler.cost()
 
 #配料 蓝莓
class Blueberry(SnackDecorator):
    def __init__(self, cooler):
        self.cooler = cooler
 
    def get_description(self):
        return self.cooler.get_description() + " + Blueberry"
 
    def cost(self):
        return 4 + self.cooler.cost()

if __name__ == '__main__':
    
    b = MuilkShake()
    print("%s = %s yuan\n" % (b.get_description(), b.cost())) 
 
    b = MuilkTea()
    b = Pearl(b)
    b = Gram(b)
    print("%s = %s yuan\n" % (b.get_description(), b.cost()))
 
    b = MuilkTea()
    b = Pearl(b)
    b = Gram(b)
    b = Blueberry(b)
    print("%s = %s yuan\n" % (b.get_description(), b.cost()))

'''
运行结果：MuilkShake = 5 yuan
          MuilkTea + Pearl + Gram = 7 yuan
          MuilkTea + Pearl + Gram + Blueberry = 11 yuan
          [Finished in 0.1s]
'''
