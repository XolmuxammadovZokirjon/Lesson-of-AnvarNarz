"""
15/07/2022

Dasturlash asoslari

# 30-DARS. VORISLIK  VA POLIMORFIZM

Muallif: Zokirjon Xolmxuammadov


"""

class Shaxs:
	"""Shaxslar haqida ma'lumot"""
	def __init__(self,ism,familiya,passport,tyil):
		"""Shaxsning xususiyatlari"""
		self.ism = ism
		self.familiya = familiya
		self.passport = passport
		self.tyil = tyil
	def get_info(self):
		"""Shaxs haqida ma'lumot"""
		info = f"{self.ism} {self.familiya}. "
		info += f"Passport: {self.passport}, {self.tyil}-yilda tu'gilgan"
		return info
	def get_age(self,yil):
		"""Shaxsning yoshini qaytaruvchi metod"""
		return yil - self.tyil


class Talaba(Shaxs):
	"""Talaba klassi"""
	def __init__(self,ism,familiya,passport,tyil,idraqam):
		"""Talabaning xususiyatlari"""
		super().__init__(ism, familiya, passport, tyil)
		self.idraqam = idraqam
		self.bosqich = 1

	def get_id(self):
		"""Talabaning ID raqami"""
		return self.idraqam
	def get_bosqich(self):
		"""Talabaning o'qish bosqichi"""
		return self.bosqich

# inson = Shaxs("Hasan","Husanov","FB001122",2000)
# print(inson.get_age(2021))

talaba1 = Talaba("Alijon","Valiyev","FF112233",2001,"N0000011")
print(talaba1.get_info())