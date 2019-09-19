from unittest import TestCase
from real_numbers import RealNumbers


class TestRealNumbers(TestCase):

	def setUp(self):
		self.x = RealNumbers()

	# x^2 -1 = 0
	def test_solve_real(self):
		x1, x2 = self.x.solve(1 , 0, -1)
		self.assertAlmostEqual(x1, -1, 2)
		self.assertAlmostEqual(x2, 1, 2)

	# x^2 + 1 = 0
	def test_solve_complex(self):
		x1, x2 = self.x.solve(1 , 0, 1)
		self.assertAlmostEqual(x1, -1, 2)
		self.assertAlmostEqual(x2, 1, 2)