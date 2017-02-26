import numpy as np
n, m = map(int, raw_input().split())
arr = np.array([map(int, raw_input().split()) for x in range(n)])

print np.mean(arr, axis = 1)
print np.var(arr, axis = 0)
print np.std(arr)
