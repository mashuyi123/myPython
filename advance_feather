#切片，slice操作符，用于经常取指定索引范围的操作
#eg:L[0:2]表示取前两个元素
# 倒数第一个元素的索引是-1
L = ['mashuyi','yangruoxi','suming','wangyixue']
print(L[0:2])
print(L[:3])
N =list(range(100))
print
print(N[10:20])
# 取前十个数，每两个取一个
print(N[:10:2])
# 取所有数，每五个取一个
print(N[::5])
print(N)
t=(0,1,3,4,5)
print(t[:3])
str = 'mashuyi'
# python没有针对字符串的截取函数，只需要切片就可以完成
print(str[0:2])
# eg:利用切片操作，实现trim(),去除字符串首尾空格
strtest1 = '  mashuyi   '
print(strtest1)
#方法1，函数实现
print(strtest1.strip())
# 方法2，切片实现
# 迭代，python中，迭代是通过for...in...完成的，其它语言，迭代是通过下标完成的
# 所以python中只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代
# 默认迭代dic跌打的是key，如果要迭代value，for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()
# 字符串也是可迭代对象，也可以作用于for循环：
for ch in 'mashuyi':
	print(ch)
# 判断对象是否是可迭代对象方法：通过collections模块的Iterable类型判断
from collections import Iterable
isinstance('mashuyi', Iterable)
# 对list实现下标循环，python内置函数enumerate，可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素
for i , value in enumerate(['A','B','C']):
	print(i,value)

def findMinAndMax(L):
	if not isinstance(L,list):
		raise TypeError('%s:is not a List'%L)    
	else:
	    if len(L)==0:
	        return('List is empty')
	    else:
	        a = L[0]   
	        b = L[0]
	        for i in L:
	            if i < a:
	                a = i
	            if i > b:
	                b = i
	    print('min:',a,'max:',b)

	return
Lin = [2,1,5,7,88]
print(findMinAndMax(Lin))
# 列表生成式
# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
print([x * x for x in range(1, 11) if x % 2 == 0])
# 列出当前目录下，所有文件和目录名
import os
d=[d for d in os.listdir('.')]
print(d)
# 把一个list中所有的字符串变成小写
name = ['MaShuYi','YangRuoXi','SuMing']
print([s.lower() for s in name]) 
# 生成器
# 边循环一边计算的机制，称为生成器：generator
# 创建一个generator，方法1：把一个列表生成式的[]改成()，就创建了一个generator
ls = [x*x for x in range(10)]
print(ls)
g = (x*x for x in range(10))
print(g)
# 打印生成器的每一个元素
# 法1：通过next()函数获得生成器的下一个返回值；法2：使用for循环
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# 生成器保存的是算法,每次调用next(g)就是计算出g的下一个元素值，知道计算到最后一个元素，没有元素时，抛出StopIteration的错误
for n in g:
	print(n)
# 一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
# 要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。
# 普通函数调用直接返回结果,generator函数的“调用”实际返回一个generator对象
# 迭代器
# 可以直接作用于for循环的数据类型有以下几种：
# 类是集合数据类型，如list、tuple、dict、set、str等；
# 一类是generator，包括生成器和带yield的generator function。
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。可以使用isinstance()判断一个对象是否是Iterable对象
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator,可以使用isinstance()判断一个对象是否是Iterator对象
from collections import Iterator
print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance('abc',Iterator))
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
# list、dict、str等Iterable变成Iterator可以使用iter()函数：
print(isinstance(iter([]), Iterator))
# 凡是可作用于for循环的对象都是Iterable类型；凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；