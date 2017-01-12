k = input()
lis = map(int, raw_input().split())
myset = set(lis)
myset_sum, lis_sum = sum(myset), sum(lis)
print (myset_sum * k - lis_sum) / (k-1)




#k = input()
#lis = raw_input().split()
#myset = set(lis)
#for i in myset:
#	try:
#		lis.remove(i)
#		lis.remove(i)
#	except:
#		print i

#k = input()
#lis = raw_input().split()
#myset = set(lis)
#for i in myset:
#	lis.remove(i)
#print list(myset.difference(set(lis)))[0]

#k = input()
#lis = raw_input().split()
#og_set = set(lis)
#for n in og_set:
#	lis.remove(n)
#	if len(og_set) != len(set(lis)):
#		print n

#k = input()
#lis = raw_input().split()
#og_set = set(lis)
#for n in og_set:
#	lis.remove(n)
#	if og_set != set(lis):
#		print n
