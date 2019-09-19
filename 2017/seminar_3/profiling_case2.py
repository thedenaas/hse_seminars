from memory_profiler import profile

@profile
def merge(left, right):

	if not len(left) or not len(right):
		return left or right

	result = []
	i, j = 0, 0
	while (len(result) < len(left) + len(right)):
		if left[i] < right[j]:
			result.append(left[i])
			i+= 1
		else:
			result.append(right[j])
			j+= 1
		if i == len(left) or j == len(right):
			result.extend(left[i:] or right[j:])
			break

	return result


def merge_sort(a):
	if len(a) < 2:
		return a

	middle = len(a) // 2
	left = merge_sort(a[:middle])
	right = merge_sort(a[middle:])

	return merge(left, right)


if __name__ == '__main__':
	import random
	random.seed(1337)
	a = [random.randint(0, 10000) for x in range(10000)]
	merge_sort(a)
