import numpy
n, m = map(int, raw_input().split())
arr = numpy.array([map(int, raw_input().split()) for x in range(n)])

print numpy.prod(numpy.sum(arr, axis = 0))
