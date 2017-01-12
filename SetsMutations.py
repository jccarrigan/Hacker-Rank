who_cares = input()
s = set(map(int, raw_input().split()))
for _ in range(input()):
	cmd = raw_input()
	cmd = cmd.split()
	evaluation = 's.%s(%s)' % (cmd[0], set(map(int, raw_input().split())))
	eval(evaluation)

print sum(s)
