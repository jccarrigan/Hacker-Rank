n_m = map(int, raw_input().split())
arr = map(int, raw_input().split())
n_set = set(map(int, raw_input().split()))
m_set = set(map(int, raw_input().split()))

happy = 0
for i in arr:
	if i in n_set:
		happy += 1
	if i in m_set:
		happy -= 1
print happy
