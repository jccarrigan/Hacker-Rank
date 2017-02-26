import numpy as np
n, m = map(int, raw_input().split())
arr = np.array([map(int, raw_input().split()) for x in range(n)])

print np.max(np.min(arr, axis = 1))
