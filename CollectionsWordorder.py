from collections import OrderedDict, Counter

ordict = OrderedDict()
input_list = []
for _ in range(input()):
    s = raw_input()
    input_list.append(s)
    ordict[s] = 0
counted = Counter(input_list)
for key in ordict.keys():
    ordict[key] = str(counted[key])
print len(ordict)
print ' '.join(ordict.values())



#ordict = OrderedDict()
#for _ in range(input()):
#    inp = raw_input()
#    if inp not in ordict.keys():
#        ordict[inp] = 1
#    else:
#        ordict[inp] += 1
#    
#print len(ordict)
#print ' '.join(map(str, ordict.values()))
