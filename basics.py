#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Python Learn record 2018/05/30
#r'',''内部的字符默认不转义
#'''...'''格式表示多行内容
#全部大写的变量名表示常量
#除法计算结果是浮点数3.0；地板除//，两个整数的除法仍然是整数
#python的整数没有大小限制，超出范围表示为inf意为无限大
#函数ord()获取字符的整数表示，chr()函数把编码转换为对应字符
#len()函数计算字符串字符数
#格式化字符串%实现
print('I\\\'m ok!') 
print(r'T\\\'m ok!')
print('mashuyi \n I\'m OK!')
print('''line
line2
line3''')
age = 25
if age >= 26:
	print(True)
else:
	print(not True)
a = 'ABC'
b = a
a = 'XYZ'
print(a+b)
print(10//3)
print("Hello,%s!you are wonderful!,This year you are %d year's old" %("mashuyi",25))
#python list and tuple
#append()-> pop() ,insert()
#tuple是有序列表的元组，一旦初始化不可修改，不可修改指的是tuple元素的指向不可修改
#定义一个tuple的时候，tuple的元素必须被确定下来
#tuple没有append(),insert(),pop()这些属性
classmates = ['Suming','Wangyixue','Yangruoxi','Mashuyi']
print(classmates[-4],len(classmates))
classmates.append('Linxi')
classmates.insert(0,'Xiaopingjing')
print(classmates)
classmates.pop()
print(classmates)
classmates.pop(0)
print(classmates)
L=[]
print(len(L))
t=()
print(t)
T = ('Xiaopingjing','Linxi','Xiaoce')
print(T)

#条件判断和循环
#这里注意一下，原来用elseif,paython里用elif
#int()作用于字符变量前可以把字符变量强制转换为int型
#Python有两种循环，for in 循环和 while 循环
#for x in...循环就是把每个元素的变量带入x,然后执行缩进快内的语句
#range()函数，生成一个整数序列,可以通过list()函数将序列转换为list,eg:range(3),生成0,1,2
#while循环，只要条件满足，就能不断循环
#break提前结束循环，continue会跳过此次循环
age = 19
if age < 12:
	print('your age is', age)
	print('child')
elif 12 <age<18:
	print('your age is', age)
	print('teenager')
else:
	print('adult')

for names in classmates:
	print(names)

sum = 0
for i in range(101):
	sum = sum + i
print(sum)

a = list(range(5))
print(a)

summ = 0
n = 9
while n > 0:
	summ += n
	n = n - 2
print(summ) 

sumBreak = 0
for i in range(5):
	sumBreak = sumBreak + i
	if(sumBreak > 4):
		break
print(sumBreak)

sumCon = 0  
while n < 10:
	n = n + 1
	if n % 2 == 0:
		continue
	print(n)

#dict和set
#dict即dictionary，其它语言中称之为map,使用键值对，查找速度快
d = {'Mashuyi':99, 'Suming':88, 'Yangruoxi':90}
print(d['Mashuyi'])
d['Wangyixue'] = 86
print(d)
#判断key值是否存在有两种方法，一种是'**' in dict,另一种是dict的get方法，key不存在返回None或者自己指定的value，返回none时python交互环境不显示
#删除一个key，可以用pop(key)方法，对应的value也会从dict中删除
print('Linxi' in d) 
print(d.get('wangyixue',-1))
d.pop('Wangyixue')
print(d)
#list比较，dict有以下几个特点：需要占用大量的内存，内存浪费多。而list相反：占用空间小，浪费内存很少。
#dict可以用在需要高速查找的很多地方，dict的key必须是不可变对象。
