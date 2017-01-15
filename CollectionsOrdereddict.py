from collections import OrderedDict

ordict = OrderedDict()
for _ in range(input()):
    inp = raw_input().split()
    key, value = ' '.join(inp[:-1]), int(inp[-1])
    if key not in ordict.keys():
        ordict[key] = value
    else:
        ordict[key] += value
    
for item in ordict.items():
    print item[0], item[1]
