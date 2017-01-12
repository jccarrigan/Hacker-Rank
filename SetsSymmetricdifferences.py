mlen = input()
m = set(map(int, raw_input().split()))
nlen = input()
n = set(map(int, raw_input().split()))

a_list = list(m.difference(n))
b_list = list(n.difference(m))

for i in sorted(a_list + b_list):
    print i
