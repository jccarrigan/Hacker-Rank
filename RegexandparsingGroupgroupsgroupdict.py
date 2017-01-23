import re

m = re.search(r'([a-zA-Z0-9])\1+', raw_input())

if m == None:
    print '-1'
else:
    print m.group(1)
