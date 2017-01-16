from collections import deque

d = deque()
for _ in range(input()):
    inp = raw_input().split()
    cmd, args = inp[0], inp[1:]
    eval('d.'+cmd+'('+','.join(args)+')')
print ' '.join(map(str, d))
