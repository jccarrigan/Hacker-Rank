from itertools import combinations_with_replacement

line = raw_input().split()
s, k = sorted(line[0]), int(line[1])
for i in list(combinations_with_replacement(s, k)):
    print ''.join(i)
