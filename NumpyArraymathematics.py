import numpy
n, m = map(int, raw_input().split())
A = numpy.array([map(int, raw_input().split()) for i in range(n)])
B = numpy.array([map(int, raw_input().split()) for i in range(n)])

print A + B
print A - B
print A * B
print A / B
print A % B
print A ** B
