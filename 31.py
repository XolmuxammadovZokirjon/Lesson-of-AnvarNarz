
from uuid import uuid4
class Avto:
	"""Avtomobil klassi"""
	num_avto = 0
	def __init__(self,make,model,rang,yil,narh,km=0):
		"""Avtomobilning xususiyatlari"""
		self.make = make
		self.model = model
		self.rang = rang
		self.yil = yil
		self.narh = narh
		self.__km = km
		self.__id = uuid4()
		Avto.num_avto += 1

	@classmethod
	def get_km(self):
		return self.__km
	
	def get_id(self):
		return self.__id

	def add_km(self,km):
		if km >= 0:
			self.__km += km
		else:
			print("Mashina km kamaytirib ")

avto1 = Avto("GM","Malibu","",2022,40000)