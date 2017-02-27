import numpy as np
n = int(raw_input())
print np.linalg.det([map(float, raw_input().split()) for x in range(n)])
