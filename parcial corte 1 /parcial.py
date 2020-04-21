from numpy import*
from math import*

class Datasp:

	def __init__(self,datos):
		self.data=datos
		self.media=0
		self.varianza=0
		self.destandar=0
		self.skew=0
		self.kurtosis=0
		self.covarianza=0
		self.correlacion=0

	def md(self):
		self.med=sum(self.data)/len(self.data)
		return(self.med)

	def vr(self):
		l=(self.data-self.med)
		m=l*l
		self.var=sum(m)/(len(self.data)-1)
		return(self.var)

	def ds(self):
		self.des=sqrt(self.var)
		return(self.des)

	def sk(self):
		self.a=(self.data - self.med)/self.des
		self.b=list(map(lambda x:x**3, self.a))
		self.skw=sum(self.b)/len(self.data)
		return(self.skw)

	def kr(self):
		self.c=list(map(lambda x:x**4, self.a))
		self.kur=(sum(self.c)/len(self.data))-3
		return(self.kur)

	def cv(self):
		self.x1=self.data[:,0]
		self.y1=self.data[:,1]
		self.x1y1=self.x1 * self.y1
		self.cov=(sum(self.x1y1)/len(self.x1y1)) - (sum(self.x1)/len(self.x1)) * (sum(self.y1)/len(self.y1))
		return(self.cov)

	def cr(self):
		self.x2=sum(self.x1)/len(self.x1)
		self.y2=sum(self.y1)/len(self.y1)
		self.xx=sum((self.x1 - self.x2)*(self.x1 - self.x2))/(len(self.x1) -1 )
		self.yy=sum((self.y1 - self.y2)*(self.y1 - self.y2))/(len(self.y1) -1 )
		self.cor=self.cov/(sqrt(self.xx)*sqrt(self.yy))
		return(self.cor)
