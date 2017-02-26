import numpy

n, m = map(int, raw_input().split())

temp = []
for _ in range(n):
    temp.append(map(int, raw_input().split()))
                
print numpy.transpose(temp)
print numpy.array(temp).flatten()
