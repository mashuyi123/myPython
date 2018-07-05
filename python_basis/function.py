#Python函数
#函数名其实就是一个函数对象的调用，可以把函数名赋值给变量，相当于给函数起了个别名
#定义函数用def语句，依次写出函数名，括号，括号中参数，冒号，缩进块中写函数体，返回值用return
#函数体内部的语句执行时，一旦执行到return,函数就执行完毕，并将结果返回，如果没有return，函数执行完毕后也会返回结果，结果为None
import sys
import math
print(sys.path)
sys.path.insert(0,'G:/python/myPython')
from abstest import myabs
from abstest import power
from abstest import register
from abstest import calc
from abstest import calsv
from abstest import persion
from abstest import persionv
from abstest import muilt
from abstest import fact
from abstest import factv
print(hex(255))
print(myabs(-7))
#空函数：占位函数pass
#内置函数isinstance()，实现对数据类型的检查myabs
#Python的函数返回多值其实就是返回一个tuple
#函数的参数
print(power(3))
print(power(3,3))
# 默认参数：可以简化函数调用
# 设置默认参数时注意：必选参数在前，默认参数在后；当有多个默认参数时，变化大的在前，变化小的在后
# Python函数在定义的时候，默认参数L的值就被计算出来了，如果默认参数是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
register('mashuyi','W')
register('yangruoxi','W','24')
register('liuhanran','M','20','安徽')
# 可变参数：即传入的参数的个数是可变的
#参数个数不确定，可以把参数作为一个list或tuple传进来,调用的时候需要先组装一个list或者tuple
# eg:计算a*a + b*b + c*c + ……
print(calc([1,2,3]))
print(calc((1,2,3,4)))
#利用可变参数,定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple
# 函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数
print(calsv(1,2,3,4,5))
# 如果已经有了一个list或者tuple，要调用可变参数，可以再list或者tuple前加一个*号，把list或tuple的元素变为可变参数传进去
nums = [1,2,3]
print(calsv(*nums))
# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
persion('mashuyi','24')
persion('yangruoxi','24',city='hangzhou')
persion('wangyixue','24',major='student',city='beijing')

extra = {'job':'enginteer','weight':'50kg'}
persion('suming','25',job=extra['job'],weight=extra['weight'])
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
persion('suming','25',**extra)
persionv('suming','25',city = 'chengdu',job = 'conter')
# 参数组合
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
muilt(2,3,4)
# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
# 要注意定义可变参数和关键字参数的语法：
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。
# 以及调用函数时如何传入可变参数和关键字参数的语法：
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
#递归函数
print(fact(5))
print(factv(6))