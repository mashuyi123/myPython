import os

# os.chdir("D:\\01mashuyi\\DailySummary\\Python\\HeadFirstPython\\chapter5")
os.chdir("G:\\00mashuyi\\DailySummary\\Python\\HeadFirstPython\\chapter6")

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
		return({'Name':temp.pop(0),
			'BIrth':temp.pop(0),
			'Times':str(sorted(set([sanitize(each) for each in temp]))[0:3])})
	except IOError as ioerr:
		print('File error:' + str(ioerr))
		return(None)

james = readData('james2.txt')
julie = readData('julie2.txt')
mikey = readData('mikey2.txt')
sarah = readData("sarah2.txt")
print(sarah)
print(sarah['Name'] + "'s fastest times are:" + sarah['Times'])
print(james['Name'] + "'s fastest times are:" + james['Times'])
print(julie['Name'] + "'s fastest times are:" + julie['Times'])
print(mikey['Name'] + "'s fastest times are:" + mikey['Times'])
