import numpy

shape = tuple(map(int, raw_input().split()))

print numpy.zeros(shape, dtype = numpy.int)
print numpy.ones(shape, dtype = numpy.int)
