a = set(raw_input().split())
condition = True
for _ in range(input()):
	b = set(raw_input().split())
	if b.difference(a) != set():
		condition = False
print condition
