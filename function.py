#Python函数
#函数名其实就是一个函数对象的调用，可以把函数名赋值给变量，相当于给函数起了个别名
#定义函数用def语句，依次写出函数名，括号，括号中参数，冒号，缩进块中写函数体，返回值用return
#函数体内部的语句执行时，一旦执行到return,函数就执行完毕，并将结果返回，如果没有return，函数执行完毕后也会返回结果，结果为None
import sys
import math
print(sys.path)
sys.path.insert(0,'G:/python/myPython')
from abstest import myabs
print(hex(255))
print(myabs(-7)
#空函数：占位函数pass
#内置函数isinstance()，实现对数据类型的检查myabs
#Python的函数返回多值其实就是返回一个tuple
