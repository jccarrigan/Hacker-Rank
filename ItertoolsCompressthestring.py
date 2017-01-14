def foo(s):
#    print s
#    print range(len(s)-1)
    count = 1
    for i in range(len(s)):
        if i == len(s) - 1:
#            print '1st check'
            yield (count, int(s[i]))
        elif s[i] == s[i+1]:
#            print '2nd check'
            count += 1
        else:
#            print '3rd check'
            yield (count, int(s[i]))
#            print 'post yield I is %s' % count
            count = 1
#            print 'post yield I is %s' % count
            
#            count = 1

#foo(raw_input())
instance = foo(raw_input())
condition = True
out = []
while condition:
    try:
        out.append(next(instance))
    except:
        condition = False
for i in range(len(out)):
    print out[i],
