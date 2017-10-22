class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
    

	def __str__(self):
		 return "Ponto(" + str(self.x) + "," + str(self.y) + ")"
		

	def __add__(self, ponto):
		return Point(self.x + ponto.x, self.y+ponto.y)