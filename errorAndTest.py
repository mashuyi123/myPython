# 跟踪程序的执行，查看变量的值是否正确，这个过程称为调试。Python的pdb可以让我们以单步方式执行代码。
# 在程序运行的过程中，如果发生了错误，可以事先约定返回一个错误代码
# 当我们认为某些代码可能会出错时，就可以用try来运行这段代码
# 如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块
# 执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。

try:
	print("try...")
	r = 10 / int('a')
	print('result:',r)
except ValueError as e:
	print('value error',e)
except ZeroDivisionError as e:
	print('except',e)
else:
    print('no error!')
finally:
	print('finally...')
print('end...')

#Python的错误其实也是class,所有的错误类型都继承自BaseException
# 如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出 
# 出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。
# Python内置的logging模块可以非常容易地记录错误信息
# 通过配置，logging还可以把错误记录到日志文件里，方便事后排查。
import logging
logging.basicConfig(level=logging.INFO)

def foo(s):
	return 10/int(s)
def bar(s):
	return foo(s)*2
def main():
	try:
		bar('0')
	except Exception as e:
		print('log')
		logging.exception(e)
main()
print('end')
# 抛出错误:因为错误是class，捕获一个错误就是捕获到该class的一个实例。
# 根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：
# 断言assert n != 0:表达式 n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
# 如果断言失败，assert语句本身就会抛出AssertionError
# 启动Python解释器时可以用-O参数来关闭assert($ python -O err.py)
def assFun(s):
	n = int(s)
	assert n != 0, 'n is zero'
	return 10/n
def main():
	foo('0')
# logging
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
# logging允许指定记录信息的级别，有debug，info，warning，error等几个级别
# Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。
# 为了编写单元测试，我们需要引入Python自带的unittest模块
