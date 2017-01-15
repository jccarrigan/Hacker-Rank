from  collections import Counter

who_cares = input()
inventory = Counter(map(int, raw_input().split()))

revenue = 0
for _ in range(input()):
    size, price = [int(x) for x in raw_input().split()]
    if inventory[size] != 0:
        revenue += price
        inventory[size] -= 1
print revenue
