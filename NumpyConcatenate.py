import numpy

n, m, p = map(int, raw_input().split())
N = numpy.array([map(int, raw_input().split()) for x in range(n)])
M = numpy.array([map(int, raw_input().split()) for x in range(m)])

print numpy.concatenate((N, M), axis = 0)
