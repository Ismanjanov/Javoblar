# Darslik Obj Class
# Boshlandi 01.11.21 10'15
import os
import time
class Dost:
	def __init__(self, isim,familiya,yill):
		self.isim = isim
		self.familiya = familiya
		self.yill = yill
	def tanishtir (self):
		return f'Men {self.isim} {self.familiya} tugulgan yilim {self.yill} yil'
	def get_name(self):
		return self.isim
	def get_fam (self):
		return self.familiya
	def yosh(self):
		return 2021 - self.yill

dost = Dost('olim','xakimov',2005)
dost1 = Dost('ozodbek', 'yusupov', 2000)
dost2 = Dost('ulugbek', 'odilov', 20001)
print('dost2')
# yakunlandi 01.11.21 11"22
