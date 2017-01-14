from itertools import combinations

line = raw_input().split()
string, k = sorted(line[0]), int(line[1])
for limit in range(1, k+1):
    for combo in list(combinations(string, limit)):
        print ''.join(combo)
