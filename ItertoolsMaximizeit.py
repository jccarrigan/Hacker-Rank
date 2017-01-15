from itertools import product

first_line = map(int, raw_input().split())
k = first_line[0]
m = first_line[1]
lis = []

for _ in range(k):
    lis.append(map(int, raw_input().split()[1:]))

def engine():
    for i in list(product(*lis)):
        yield i

def square(some_tuple):
    out = 0
    for x in some_tuple:
        out += x ** 2
    return out
        
instance = engine()
maximum = 0
condition = True
while condition:
    try:
        for _ in range(k):
            num = square(next(instance))
            if (num % m) > maximum:
                maximum = (num % m)
    except:
        condition = False
        print maximum
