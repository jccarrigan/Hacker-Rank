from collections import deque

for _ in range(input()):
    n, d, side = input(), deque(map(int, raw_input().split())), 2147483648
    while n > 1:
        left, right = d[0], d[-1]
        if left >= right and left <= side:
            side, n = left, n - 1
            d.popleft()
        elif right >= left and right <= side:
            side, n = right, n - 1
            d.pop()
        else:
            n = 0
    if n == 0:
        print 'No'
    else:
        print 'Yes'



#for _ in range(input()):
#    n, arr, side = input(), map(int, raw_input().split()), 2 ** 31
#    while n > 1:
#        left, right = arr[0], arr[-1]
#        if left >= right and left <= side:
#            side, arr, n = left, arr[1:], n - 1
#        elif right >= left and right <= side:
#            side, n = right, n - 1
#            arr.pop()
#        else:
#            n = 0
#    if n == 1:
#        print 'Yes'
#    else:
#        print 'No'
