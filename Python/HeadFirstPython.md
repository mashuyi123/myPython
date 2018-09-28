支持网站：http://python.itcarlow.ie/resources.html

## 第二章 ##
### IDLE使用技巧 ###
1、IDLE使用颜色区分显示代码：内置函数紫色、字符串绿色、关键字橙色、生成结果蓝色。

2、键入一些代码，TAB键，代码建议或补全。

3、IDEL shell提供python方法函数有关文档，在help->Python Docs中，F1也可查看

4、Alt+p 回退操作，Alt+n 下一步操作（IDLE的会话管理实现）

### python基本语法 ###
1、python的变量标识符没有类型。

2、python列表

- python可变列表是一个数据集合，数据项之间用逗号分隔，整个列表用中括号包围。

		python中创建一个列表，解释器会在内存中创建一个类似数组的数据结构来存储数据，数据项自下而上堆放，形成堆栈。
		listA.append("foot") //在列表末尾增加数据
		listA.pop() //在列表末尾删除数据
		listA.extend(["book","drink"]) //在列表中追加一个列表
		listA.remove("book") //在列表中删除某一特定项目
		listA.insert(0,"bread") //在某个特定位置前增加一个数据
		len(listA) //可以统计列表中数据项的个数
- python中不可变列表是指元组数据集合，一旦列表数据赋值给一个元祖，将不能再改变，列表使用小括号包围。

3、使用while和for都是为了处理迭代结构的数据，但是while使用时要有状态信息（count）,for循环由python解释器考虑状态信息。

4、isinstance() 允许检查某个特定标识符是否包含某个特定类型的数据，eg: isinstance(names,list)，返回true。

	python中有70多个BIF（内置函数），在IDE shell中，键入dir(__builtins__)可以看到python提供的内置方法列表；
	小写单词都是BIF，查看某个BIF功能。在shell中键入help(input)，就能得到确切BIF功能描述。
![](https://i.imgur.com/R2IdIjm.png)

5、用IDLE执行模块，导入文件后，按F5调用即可。
![](https://i.imgur.com/wRjTNab.png)

6、发布模块到本地副本
	
- 为模块创建一个文件夹，并把代码放在里面；
- 在新文件夹中国创建一个名为"setup.py"的文件，该文件包含发布相关的元数据，也放在创立的文件夹中，如图：

![](https://i.imgur.com/yWT9ooJ.png)

- 发布：完成后模块已经转换为发布，安装在本地副本上。

		python setup.py sdist
		python setup.py install (linux环境中：sudo python3 setup.py install）
	
![](https://i.imgur.com/4oKWEqa.png)
![](https://i.imgur.com/ryCZXPt.png)

- 导入模块就可以使用了：import nester

		使用模块时要注意命名空间的问题，命令空间就像是姓氏；
		在某个命名空间中想指示另外一个模块命名空间中的某个函数，就需要用该模块的命名空间对这个函数的调用做出限定。
7、python常用BIF

	range() //返回一个迭代器，根据需要生成一个指定范围的数字
	enumerate() //创建成对数据的一个编号列表，从0开始
	id() //返回一个python数据对象的唯一标识
	next() //返回一个可迭代数据对象如列表的下一项eg:range(3)生成0/1/2
	print() //print()函数有一个参数end=""，会关闭print函数的默认换行行为
	locals() //BIF返回当前作用域中定义的所有名的一个集合（可用以查看文件对象是否存在等）

8、函数可选参数

	为函数参数提供一个缺省值，这个参数就变为可选参数，调用时，没有该参数，则默认缺省值，有则使用提供的值。
	
## 第三章 文件与异常 ##
### 打开文件并读取 ###
1、文件打开、读取与关闭	

	import os //导入OS模块；
	os.getcwd() //获取当前工作目录；
	os.chdir("D:\\01mashuyi\\DailySummary\\Python\\HeadFirstPython\\chapter3") //切换至读取文件所在目录
	os.path.exists("test.txt") //确认需要打开的文件是否存在
	data = open("test.txt") //打开文件，并复制给名为data的文件对象
	print(data.readline(),end = "") //获取一行数据
	data.seek(0) //返回文件起始位置
	for each_line in data: //使用迭代打印文件数据
	data.close() //关闭文件
2、查看与处理数据

	split()方法：分解字符串，返回字符串列表
	(name,language) = each_line.split(":") //多重赋值
	python字符串的find()方法，查找字符串中的子串，如果无法找到，返回-1，如果找到，返回第一个该子串在原字符串中的索引位置
	strip()方法从字符串中去除不想要的空白
3、异常捕获

	为避免程序崩溃，在发生异常时将其捕获，使得程序能恢复正常运行。
	一般异常：
			try:
				code
			except:
				recoverd code
	找出需要保护，可能会发生异常的代码；
	指定异常：即指定要处理的运行时的错误类型
			try:
				code
			except IOError:
				recoverd code
	扩展异常：指异常处理程序中有一些代码希望发生了异常也必须执行，不能跳过
			try:
				code
			except ValueError:
				recoverd code
			finally:
				code
	产生一个异常时，python解释器会将一个异常对象传入这个except组，为异常对象指定一个名字，然后异常对象就可作为错误消息的一部分
			except IOErrpr as err:
				print("File error:" + str(err))
		
					
## 第四章 持久存储  ##
### 数据保存到文件 ###
1、持久存储：指将处理后的基于内存的数据存储在磁盘上。
2、以写模式打开文件：

	open()默认以读的方式打开文件，所以不用显式指定；
	out = open("test.txt","w")
	print("Test writtinh!", file = out) //out表示所写数据文件对象的名
	out.close() //完成数据写入时，一定要关闭文件，实现刷新输出,如果写入过程中出现异常，关闭文件可能无法执行，此时需要加异常处理，把关闭文件操作移动到异常处理Finally中
	使用访问方式为w时，打开指定文件写，若文件已存在，则覆盖写入，若文件不存在，则会创建文件
	使用访问方式为a时，打开指定文件追加写入
	使用访问方式w+，打开指定文件完成读和写
	print("test",file = fh) //file参数控制将数据发送/保存到哪里
### python基础知识 ###
1、Python变量只是包含一个数据对象的引用，数据对象才真正包含数据，Python的内存管理技术会回收所使用的RAM。当没有数据对象指示某个变量时，Python会将它回收，如果想改变一个不可变的值，Python会提示TypeError。

2、Python中不可变的数据类型：元组、字符串、数值类型等。
### 用with处理文件 ###
1、使用with时，不用用finally关闭打开的文件，python解释器会自动关闭（with语句利用了上下文管理协议的python技术）

	try:
		data = open("test.txt","w")
		print("It's a ...",file = data)
	except IOError as err:
		print("File error:" + str(err))
	finally:
		if "data" in locals():
			data.close()
相当于：

	try:
		with open("text.txt","w") as data:
			print("It's a ...",file = data)
	except IOError as err:
		print("File error:" + str(err))
			
2、标准输出

	sys.stdout //print()写数据的默认位置是屏幕即标准输出
3、python标准库：pickle，可保存加载任何python数据对象。
	
	import pickle；
	**pickle.dump(obj, file, protocol=None,)**
    	必填参数obj表示将要封装的对象
		必填参数file表示obj要写入的文件对象，file必须以二进制可写模式打开，即“wb”
	**pickle.load(file,*,fix_imports=True, encoding="ASCII", errors="strict")**
    	必填参数file必须以二进制可读模式打开，即“rb”，其他都为可选参数
	使用dump()保存数据，使用load()恢复数据；
	腌制或者解腌制异常：PickleError
## 第五章 推导数据 ##
### 处理数据 ###
1、python中的数据排序

	原地排序：按指定的顺序排序，排序后的数据替换原数据，对于列表，sort()提供原地排序；
	复制排序：按指定的顺序排序，排序后返回原数据的一个有序副本，sorted()BIF支持复制排序；
	默认sort()方法和sorted()BIF会按照升序排序，如果需要降序，则传入参数reverse = True.
2、方法串链从左向右读，函数串链从右向左读

3、列表推导：减少从一个列表转换为另一个列表时所需要的代码量

	原转换过程：
		创建一个新列表存放转换后的数据；
		迭代处理原列表中各个数据项；
		每次迭代时完成转换；
		将转换后的数据追加到新列表.
	eg:
		jamesData = []
		for each in james:
			jamesData.append(sanitize(each))
	使用列表推导：
		jamesData = [sanitize(each) for each in james]
	eg:分转换为秒
		mins = [1,2,3]
		secs = [each * 60 for each in mins]
		secs = [60, 120, 180]
	eg:大小写转换
		lower = ["I","don't", "like","spam"]
		upper = [s.upper() for s in lower]
		upper =['I', "DON'T", 'LIKE', 'SPAM']
4、访问列表数据：单个访问或者使用列表分片
	
	james[0];james[1]
	james[0:2]

5、删除列表重复项

	法一：
	a = [1,2,3,4,1,2,3]
	b = []
	for each in a:
		if each not in b:
			b.aappend(each)
	print(b) // b = [1,2,3] 
	法二：用集合删除列表重复项
	b = set(a)	
6、python中的集合
	
	python中的集合，数据项时无序的，且数据项不允许重复，如果试图加入一个重复的数据，python会将其忽略.
	set() //set()BIF用于创建一个空集合
	distances = set()
	distances = {10.6,3.2,11,8,1,3.2} //提供的重复项会被忽略
7、工厂函数
	
	工厂函数用于创建某种类型的新的数据项. //set()就是一个工厂函数，创建新的集合.
## 第六章 打包代码与数据 ##
### python数据结构之字典 ###
1、pop()方法从指定的列表位置删除并返回一个数据项

2、字典是内置的数据结构，允许数据与键关联，而不是数字。字典不会维护插入顺序，而会维护关联关系。
	
	a = student{}; //创建空字典
	b = dict()； //创建空字典
### python数据结构之类 ###
1、面向对象，代码称为类的方法，数据称为类的属性，实例化的数据对象称为实例。对象由类创建，各个实例的方法相同，各个对象的属性（数据）不同。

2、类的定义：

	class Athlete:
		def __init__(self): //类的初始化方法，可控制初始化对象。
			# Code Method //初始化对象的方法
	a = Athlete() //定义一个类实际是定制一个工厂函数，使用这个工厂函数创建实例，目标标识符 a 传至self参数。
	类的每个方法的第一个参数为调用对象的实例。
	在各个对象的属性中保留原始数据，可以支持类的扩展来满足其它需求。
3、类的继承
	
	class NamedList(list): //派生list类
		def __init__(self,a_name):
			list,__init__([])
			self.name = a_name //初始化派生的类，把参数赋值至属性
	mayi = NamedList("mayi")
	dir(mayi)
![](https://i.imgur.com/I1YVrtf.png)
## 第七章 web开发 ##
P253