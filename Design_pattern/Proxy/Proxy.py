#encoding=utf-8

# 国内无法访问google,必须通过shadowsock才能访问google

__author__ = 'mashuyi'
from abc import ABCMeta, abstractmethod

class Google(str):
	def __init__(self, name):
		self.name = name

class Access():
	__metaclass__ = ABCMeta

	@abstractmethod
	def visit(self):
		pass

class Home_access(Access):
	def __init__(self,name,google_A):
		self.name = name
		self.google_A = Google(google_A)

	def visit(self):
	    print("2 *** "+self.name+' *** access *** '+ self.google_A )

class Proxy(Access):
	def __init__(self, name,proxyed_name,google_A):
		self.name = name
		self.proxyed = Home_access(proxyed_name,google_A)

	def visit(self):
		self.proxyed.visit()
		print("1 *** "+self.name+" *** access ***" +self.proxyed.google_A)

if __name__ == '__main__':
	p = Proxy('shadowsock','home','Google')
	p.visit()
	
'''
		2 *** home *** access *** Google
		1 *** shadowsock *** access ***Google
		[Finished in 0.1s]
'''