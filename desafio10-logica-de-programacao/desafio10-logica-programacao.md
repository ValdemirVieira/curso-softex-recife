# Desafio de Projeto 10

## Lógica de Programação

class NumCplx:

	def __init__(self, real, img):
		self.a = complex(2,4)
		self.b = complex(5,6)
		self.c = complex(8,9)		

	def getNumC(self):
		return print(self.a, self.b, self.c)
		
	def setNumC(self, a, b, c):
		print(self.a + self.b + self.c)
		print(self.c - self.a - self.b)
		print(self.b * self.c * self.a)
		print(self.a / self.b / self.c)

res = NumCplx(setNumC())