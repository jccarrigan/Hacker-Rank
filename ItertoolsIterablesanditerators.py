from itertools import permutations

def foo(l, kay):
    for i in list(permutations(l,kay)):
        yield i

n = input()
lis = raw_input().split()
k = input()

total = 0.0
tally = 0.0

instance = foo(lis, k)
condition = True

if list(set(lis)) == ['a']:
    print float(1.0)
elif n == k:
    if 'a' in lis:
        print float(1.0)
    elif 'a' not in lis:
        print float(0.0)
else:
    while condition:
        try:
            var = next(instance)
            total += 1
            if 'a' in var:
                tally += 1
        except:
            condition = False
    print tally/total

#for perm in list(permutations(lis,k)):
#    print perm
#    total += 1
#    if 'a' in perm:
#        tally += 1
