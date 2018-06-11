# 面向对象编程，一个对象包含了数据和操作数据的函数
# python中所有数据类型都可以视为对象，自定义对象相当于面向对象编程中的类
std1 = {'name':'mashuyi','score': 99}
std2 = {'name':'suming','score': 88}
# 面向过程编程
def print_score(std):
	print('%s:%s' % (std['name'],std['score']))
print_score(std1)

# 面向对象编程
# 思维流程，将student视为一个对象，有name和score两个属性，然后创建student实体，给实体发一个打印消息，让实体自己把自己的数据打印出来
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))# 给对象发消息实际就是调用对象对应的关联函数，即对象的方法
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
# 面向对象的设计思想是抽象出Class，根据Class创建Instance