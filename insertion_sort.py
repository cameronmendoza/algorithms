seq =  [76, 64, 56, 23, 42, 11, 15, 18, 62, 72, 63, 6, 73, 43, 97, 85, 67, 38, 41, 31, 25, 5, 93, 91, 74, 12, 52, 37, 81, 26, 65, 4, 7, 61, 13, 96, 71, 45, 59, 14, 10, 100, 57, 82, 33, 49, 94, 88, 8, 32]

def sort(array):
	for j in xrange(1, len(array)):
		key = array[j]
		i = j - 1
		while i >= 0 and array[i] > key:
			array[i + 1] = array[i]
			i = i - 1
		array[i + 1] = key

sort(seq)
print seq