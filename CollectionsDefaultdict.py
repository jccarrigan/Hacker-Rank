from collections import defaultdict

n, m = [int(x) for x in raw_input().split()]
A = defaultdict(list)
for i in range(1, n+1):
    A[raw_input()].append(i)
for j in range(m):
    inp = raw_input()
    if inp not in A.keys():
        print '-1'
    else:
        print ' '.join(map(str, A[inp]))
