from itertools import permutations
line = raw_input().split()
s, k = sorted(line[0]), int(line[1])
for i in list(permutations(s, k)):
    print ''.join(i)
