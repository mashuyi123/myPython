# 函数式编程：允许把函数本身作为一个参数传入另一个函数，允许返回另一个函数
# 函数本身可以赋值给变量，即变量可以指向函数，eg: f = abs ，f(-10) = 10
# 函数名就是指向函数的变量
# 高阶函数：一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数,编写高阶函数，就是让函数的参数能够接收别的函数

def add(x,y,f):
	return f(x)+f(y)
print(add(-5,6,abs))

# map()函数，接受两个参数，一个函数，一个Iterable，map将传入的函数依次作用于序列的每个元素，并把结果作为新的Iterator返回
# eg：f(x)=x*x,把这个函数作用在list[1,2,3,4,5,6]上，用map()实现
def f(x):
	return x*x
r = map(f,[1,2,3,4,5,6])
print(list(r))
# map()函数把运算规则抽象化了，eg:把list所有数字转化为字符串
L=list(map(str,[1,'abc','mashuiyi',22]))
print(L)
# reduce()函数，把一个函数作用在一个序列上，接受两个参数，reduce把结果和序列的下一个元素做累积运算
# eg:序列求和，reduce实现
from functools import reduce
def add(x,y):
	return x+y
sum = reduce(add,[1,3,5,7,9])
print(sum)

# filter()函数用于过滤序列,filter()也接收一个函数和一个序列filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
# eg；序列中只保留奇数,去掉偶数
def is_odd(n):
	return n % 2 == 1
odd = list(filter(is_odd,[1,2,3,4,5,6,7,8]))
print(odd)

# 去掉序列中空字符串
def is_null(str):
	if str != ' ':
		return str
stri = list(filter(is_null,[' ','','mashuyi','suming']))
print(stri,len(stri))

# 排序算法
# python内置的sorted()函数可以对list进行排序
# sorted()函数也是一个高阶函数，可接受一个key函数实现自定义排序,key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted([-2,33,5,66,-67,37],reverse = True))
# eg：按绝对值大小排序
print(sorted([-2,33,5,66,-67,37],key=abs))
# 实现字符串忽略大小写排序，字符串排序实际就是字母的ascii码排序
print(sorted(['mashuyi','Yangruoxi','Suming','wangyixue'],key=str.lower, reverse = True))

# 返回函数：高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回

