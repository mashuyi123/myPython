def myabs(x):
	if not isinstance(x,(int,float)):
		raise TypeError("bad operand type")
	if(x < 0):
		return -x
	else:
		return x

def power(x,n = 2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s
#eg:学生注册函数，设置姓名和性别为必填，其它为选填
def register(name,gender,age=18,city="西安"):
	print("name:",name)
	print("gender:",gender)
	print("age:",age)
	print("city:",city)

def calc(number):
	sum = 0
	for n in number:
		sum = sum + n * n
	return sum

def calsv(*number):
	sum = 0
	for n in number:
		sum = sum + n * n
	return sum
def persion(name,age,**kw):
	# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查
	if 'city' in kw:
		pass
	if 'job' in kw:
		pass
	print("name:",name,"age:",age,"other:",kw)

# 参数限制
# 如果要限制关键字参数的名字，就可以用命名关键字参数
# 命名关键字参数必须传入参数名
# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
# eg:def person(name, age, *args, city, job):
# eg：只接收city和job作为关键字参数
# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数
def persionv (name,age,*,city,job):
	print('name:',name,'age:',age,'city:',city,'job:',job)

def muilt(*num):
	sum = 1
	for n in num:
		sum = sum*n
	return print(sum)

def fact(n):
	if n==1:
		return 1
	return n * fact(n - 1)
# 使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
# 解决递归调用栈溢出的方法是通过尾递归优化,尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况
def factv(n):
	return fact_iter(n,1)
def fact_iter(num,product):
	if num == 1:
		return product
	return fact_iter(num -1,num * product)