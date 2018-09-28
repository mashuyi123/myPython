import pickle
from Athlete_Class import Athlete

import os

# 打开文件
# os.chdir("D:\\01mashuyi\\DailySummary\\Python\\HeadFirstPython\\chapter6")
os.chdir("G:\\00mashuyi\\DailySummary\\Python\\HeadFirstPython\\chapter7")


def get_coach_data(filename):
	try:
		with open(filename) as readFile:
			data = readFile.readline()
			temp = data.strip().split(',')
		return(Athlete(temp.pop(0),temp.pop(0),temp))
	except IOError as ioerr:
		print('File error:' + str(ioerr))
		return(None)

def put_to_store(files_list):
	all_athletes = {}
	for each_file in files_list:
		ath = get_coach_data(each_file)
		all_athletes[ath.name] = ath

	try:
		with open('athletes.pickle','wb') as athf:
			pickle.dump(all_athletes, athf)
	except IOError as ioerr:
		print('File error(put_and_store):' + str(ioerr))
	return(all_athletes)

def get_from_store():
	all_athletes = {}
	try:
		with open('athletes.pickle','wb') as athf:
			all_athletes = pickle.load(athf)
	except IOError as ioerr:
		print('File error(get_and_store):' + str(ioerr))
	return(all_athletes)

the_files = ['sarah.txt','james.txt','mikey.txt','julie.txt']
data = put_to_store(the_files)

for each in data:
	print(data[each].name + " " + data[each].dob)
