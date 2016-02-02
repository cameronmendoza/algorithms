from random import randint
seq =  [76, 64, 56, 23, 42, 11, 15, 18, 62, 72, 63, 6, 73, 43, 97, 85, 67, 38, 41, 31, 25, 5, 93, 91, 74, 12, 52, 37, 81, 26, 65, 4, 7, 61, 13, 96, 71, 45, 59, 14, 10, 100, 57, 82, 33, 49, 94, 88, 8, 32]

'''

using randomized version for pivot selection
we expect split of input array to be reasonably well balanced on average

'''

'''
    Quicksort performance heavily dependent on selection of pivot


    O(n^2) worst case
    O(n log n) average case

    Divide and Conquer
    Divide: Permute array into two (possibly empty) subarrays A[p..q-1] and A[q+1..r]
    Conquer: Sort subarrays by recursive calls to quicksort
    Combine: Since subarrays already sorted, no work needed, entire array sorted
'''

def quick_sort(A, first, last):
    if first < last: # base case - single element
        pivot = randomized_partition(A, first, last)
        quick_sort(A, first, pivot - 1)
        quick_sort(A, pivot + 1, last)

def randomized_partition(A, first, last):
    i = randint(first, last)
    A[last], A[i] = A[i], A[last]
    return partition(A, first, last)


'''
    As partition procedure runs, it partitions the array into four (possibly empty) regions.
'''
def partition(A, first, last):
    x = A[last] # pivot element around which to partition the subarray, A[first..last]
    i = first - 1
    for j in xrange(first, last):
        if A[j] <= x: # partition into smaller OR larger values than x
            i += 1
            A[i], A[j] = A[j], A[i]
    ''' Pivot element swapped so that it lies between partitions correctly '''
    A[i + 1], A[last] = A[last], A[i + 1] # swap pivot element with leftmost element greater than x (initial pivot), therefore moving pivot into correct place in partitioned array

    return i + 1 # return pivot's new index

quick_sort(seq, 0, len(seq) - 1)
print seq