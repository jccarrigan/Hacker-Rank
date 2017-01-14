from itertools import product
A, B = map(int, raw_input().split()), map(int, raw_input().split())

for coord in list(product(A, B)):
    print coord,
