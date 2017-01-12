import math
ab, bc = input(), input()
print '%s°' % int(round(math.degrees(math.atan(ab/bc))))

############ WHAT IS BELOW IS WHAT I TURNED IN BUT THERE IS A KNOWN BUG IN THIS CHALLENGE THAT PREVENTS MINE FROM WORKING #######


import math

degree_sign= u'\N{DEGREE SIGN}'

AB = int(raw_input())
BC = int(raw_input())
hyp = math.pow(((AB*AB) + (BC*BC)), 0.5)

num = (BC*BC) + (hyp*hyp) - (AB*AB)
den = (2*(BC*hyp))
angle_C = math.degrees(math.acos(num/den))

print (str(int(round(angle_C))) + degree_sign)
