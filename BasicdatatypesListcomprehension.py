x = int(raw_input())
y = int(raw_input())
z = int(raw_input())
n = int(raw_input())
x_list = [a for a in range(x+1)]
y_list = [b for b in range(y+1)]
z_list = [c for c in range(z+1)]

def engine(a, b, c):
	for i in a:
		for j in b:
			for k in c:
				yield [i, j, k]
				
instance = engine(x_list, y_list, z_list)

perms = []
condition = True
while condition:
	try:
		current_next = next(instance)
		if sum(current_next) != n:
			perms.append(current_next)
	except:
		condition = False
		
print perms
