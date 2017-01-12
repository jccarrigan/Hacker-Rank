# Please note if you are reading this file that currently this challenge is only solvable in python 3
# Thus, I believe this code to work as well as it can for python 2
# This was assumed 1/12/17

def merge_the_tools(st, kay):
	n = len(st)
	chunk = n / kay

	for i in range(kay):
		thing = string[(i * chunk):((i+1) * chunk)]
		out = []
		for j in range(chunk):
			if thing[j] not in out:
				out.append(thing[j])
		print ''.join(out)
