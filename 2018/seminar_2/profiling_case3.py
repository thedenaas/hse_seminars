from memory_profiler import profile

class Storage:
	def __init__(self):
		self.s = {}

	def get(self, key):
		if key in self.s:
			return self.s[key]

	def update(self, key, value):
		self.s[key]=value

	def delete(self, key):
		if key not in self.s:
			return None
		r = self.s[key]
		del self.s[key]
		return r


@profile
def main():
	import random
	random.seed(1337)
	s = Storage()
	for x in range(10):
		s.update(str(random.randint(0, 10)), [random.randint(0, 1000)]*1000000)
		s.delete(str(random.randint(0, 10)))


if __name__ == '__main__':
	main()