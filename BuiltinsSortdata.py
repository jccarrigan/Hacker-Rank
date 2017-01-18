n, m = [x for x in map(int, raw_input().split())]

l = []

for _ in range(n):
    l.append(map(int, raw_input().split()))

k = int(raw_input())
    
def chooser(string):
    return string[k]

sorted_l = sorted(l, key = chooser)

for nums in sorted_l:
    print ' '.join(str(x) for x in nums)
