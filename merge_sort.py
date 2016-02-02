import sys

sequence =  [76, 64, 56, 23, 42, 11, 15, 18, 62, 72, 63, 6, 73, 43, 97, 85, 67, 38, 41, 31, 25, 5, 93, 91, 74, 12, 52, 37, 81, 26, 65, 4, 7, 61, 13, 96, 71, 45, 59, 14, 10, 100, 57, 82, 33, 49, 94, 88, 8, 32]

def merge_sort(A, first, last):
	if first < last:
		middle = (first + last) // 2
		merge_sort(A, first, middle)
		if middle > first:
			merge_sort(A, middle, last)
		merge(A, first, middle, last)

def merge(A, first, middle, last):
	L = A[first:middle]
	R = A[middle:last]

	L.append(sys.maxint)
	R.append(sys.maxint)

	i = 0
	j = 0
	for k in range(first, last):
		if L[i] <= R[j]:
			A[k] = L[i]
			i = i + 1
		else:
			A[k] = R[j]
			j = j + 1

merge_sort(sequence, 0, len(sequence))
print sequence
