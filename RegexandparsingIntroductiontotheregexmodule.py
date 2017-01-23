import re

for _ in range(int(raw_input())):
    print bool(re.match(r'[-+]?\d*\.\d*$', raw_input()))
