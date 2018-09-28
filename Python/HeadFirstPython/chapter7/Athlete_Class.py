import os

# 打开文件
# os.chdir("D:\\01mashuyi\\DailySummary\\Python\\HeadFirstPython\\chapter6")
os.chdir("G:\\00mashuyi\\DailySummary\\Python\\HeadFirstPython\\chapter7")

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
