from memory_profiler import profile

@profile
def bubble_sort(a):
	for j in range(len(a)-1, 0, -1):
		for i in range(j):
			if a[i]>a[i+1]:
				a[i], a[i+1] = a[i+1], a[i]
	return a


if __name__ == '__main__':
	import random
	random.seed(1337)
	a = [random.randint(0, 10000) for x in range(10000)]
	bubble_sort(a)