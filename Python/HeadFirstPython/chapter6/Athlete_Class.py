import os

# 打开文件
# os.chdir("D:\\01mashuyi\\DailySummary\\Python\\HeadFirstPython\\chapter6")
os.chdir("G:\\00mashuyi\\DailySummary\\Python\\HeadFirstPython\\chapter6")

# 定义运动员类
class Athlete:
	def __init__(self, a_name, a_dob = None, a_times = []):
		self.name = a_name
		self.dob = a_dob

# 返回最快的三个时间
	

class Athlete(list):
	def __init__(self,a_name, a_dob= None,a_times = []):
		list.__init__([])
		self.name = a_name
		self.dob = a_dob
		self.extend(a_times)

	def top3(self):
		return (sorted(set([sanitize(each) for each in self ]))[0:3])

# 函数用来过滤'-'和':'不标准的字符串数据
def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'	
	else:
		return(time_string)
	(mins,secs) = time_string.split(splitter)
	return(mins + '.' +secs)

# 打开文件读取数据的函数
sarah = []
def readData(fileName):
	try:
		with open(fileName) as readFile:
			data = readFile.readline()
			temp = data.strip().split(',')
		return(Athlete(temp.pop(0),temp.pop(0),temp))
	except IOError as ioerr:
		print('File error:' + str(ioerr))
		return(None)


vera = Athlete('Vera Vi')
vera.append('1.31')
print(vera.top3())
vera.extend(['2.30','1-21','2:22'])
print(vera.top3())

james = readData('james2.txt')
julie = readData('julie2.txt')
mikey = readData('mikey2.txt')
sarah = readData("sarah2.txt")

print(sarah.name + "'s fastest times are:" + str(sarah.top3()))
print(james.name + "'s fastest times are:" + str(james.top3()))
print(julie.name + "'s fastest times are:" + str(julie.top3()))
print(mikey.name + "'s fastest times are:" + str(mikey.top3()))
