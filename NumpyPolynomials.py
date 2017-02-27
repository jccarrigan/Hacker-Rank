poly = map(float, raw_input().split())[::-1]
x = float(raw_input())

y = 0
for n in range(len(poly)):
    y += poly[n]*(x**n)
print y
