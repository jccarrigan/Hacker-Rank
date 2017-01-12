who_cares = input()
s = set(map(int, raw_input().split()))
for _ in range(input()):
	cmd = raw_input()
	if cmd == 'pop':
		s.pop()
	else:
		cmd = cmd.split()
		evaluation = 's.%s(%s)' % (cmd[0], cmd[1])
		eval(evaluation)

print sum(s)
