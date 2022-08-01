"""
13/07/2022

Dasturlash asoslari

29-DARS. OBYEKTLAR BILAN ISHLASH

Muallif: Zokirjon Xolmuxammadov


"""

class Talaba:
	"""Talaba nomli klass yaratamiz"""
	def __init__(self,ism,familiya,tyil):
		"""Talabaning xususiyatlari"""
		self.ism = ism
		self.familiya = familiya
		self.tyil = tyil
		self.bosqich = 2

	def get_info(self):
		"""Talaba haqida ma'lumot"""
		return f"{self.ism} {self.familiya}. {self.bosqich}-talabasi "
	def get_name(self):
		"""Talabaning ismini qaytaradi"""
		return self.ism
	def get_lastname(self):
		"""Talabaning familiyasini qaytaradi """
		return self.familiya
talaba1 = Talaba("Alijon","Valiyev",1995)
print(talaba1.get_info())