inp = map(int, raw_input().split())
N, X, subject_list = inp[0], inp[1], []

for _ in range(X):
    subject_list.append(map(float, raw_input().split()))
    
for i in zip(*subject_list):
    print sum(i)/len(i)
