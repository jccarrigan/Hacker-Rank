import re

split_list = re.split('[,\.]*', raw_input())

for i in split_list:
    if len(i) != 0:
        print i
