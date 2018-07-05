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

    def get_grade(self):
    	if self.score > 90 :
    		return 'A'
    	elif self.score > 60 :
    		return 'B'
    	else:
    		return 'C'

    def print_score(self):
        print('%s: %s' % (self.name, self.score))# 给对象发消息实际就是调用对象对应的关联函数，即对象的方法
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
print(lisa.get_grade())
# 面向对象的设计思想是抽象出Class，根据Class创建Instance
# 特殊方法“__init__”前后分别有两个下划线！！！
# __init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
# 在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量
class Sstudent(object):

	def __init__(self, name, score):
		self.__name = name
		self.__score = score
	def getName(self):
		return self.__name
	def getScore(self):
		return self.__score
	def setName(self,name):
		self.__name = name
	def setScore(self,score):
		self.__score = score
	def printStu(self):
		print(self.__name,self.__score)

stu = Sstudent('mashuyi', 86)
print(stu.getName(),stu.getScore())
stu.setName('yangruoxi')
stu.setScore(92)
stu.printStu()
# 判断一个变量是否是某个类型可以用isinstance()
# eg:isinstance(a,Animal)
print(isinstance(stu,Sstudent))
# 在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类
# Python:动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的
print(type(stu))
print(type(1123))
print(isinstance(1123,int))
# 用type方法可以来判断对象引用的类型，有哪些方法
# 能用type()判断的基本类型也可以用isinstance()判断
# 比较两个对象类型是否相同
print(type(123) == type(345))
# 判断一个对象是否是函数，使用types模块中定义的常量
import types
def fn():
	pass
print(type(fn) == types.FunctionType)
print(type(stu.setName))
# 方法不是函数
print(type(stu.setName) == types.FunctionType)
print(type(abs))
print(type(abs) == types.BuiltinFunctionType)
# 对于继承关系，判断class类型，使用isinstance()方法
# isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上
# 优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”
print(isinstance([1,2,3],(list,tuple)))
# 获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
print(dir(stu))
# getattr()、setattr()以及hasattr()
# 可以传入一个default参数，如果属性不存在，就返回默认值
# getattr(obj,'z',404)
# 在编写程序的时候，千万不要对实例属性和类属性使用相同的名字
# 因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性
# 实例属性属于各个实例所有，互不干扰

