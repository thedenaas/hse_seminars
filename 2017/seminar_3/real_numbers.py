import math


class RealNumbers:
	def __init__(self):
		self.pi = 3.14

	def solve(self, a, b, c):
		d = math.sqrt(b ** 2 - 4 * a * c)
		x1 = (-b - d) / 2
		x2 = (-b + d) / 2
		return x1, x2