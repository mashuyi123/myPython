#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 开始学习模块，啦啦啦啦
# 在Python中，一个.py文件就称之为一个模块（Module）
# 为了避免模块名冲突，Python引入了按目录来组织模块的方法，称为包（Package）
# 每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。
# __init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块
# 自己创建模块时要注意命名，不能和Python自带的模块名称冲突。例如，系统自带了sys模块，自己的模块就不可命名为sys.py，否则将无法导入系统自带的sys模块。
# 模块名不要和系统模块名冲突，最好先查看系统是否已存在该模块，检查方法是在Python交互环境执行import abc，若成功则说明系统存在此模块

' a test module '  #表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

__author__ = 'Michael Liao'

import sys
# 导入sys模块后，有了变量sys指向该模块，可以访问sys模块的所有功能
# sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，第一个参数永远是该.py文件的名称
# 运行python3 hello.py获得的sys.argv就是['hello.py']

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')
# 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
# 而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。


if __name__=='__main__':
    test()
# 在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。
# 在Python中，是通过_前缀来实现的
# 正常的函数和变量名是公开的（public），可以被直接引用
# __xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，Python并没有一种方法可以完全限制访问private函数或变量
# 代码封装：外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public

# 在Python中，安装第三方模块，是通过包管理工具pip完成的
