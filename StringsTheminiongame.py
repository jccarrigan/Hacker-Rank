vowel = list('AEIOU')

def minion_game(st):
	kevin, stuart = 0, 0
	length = len(st)
	for i in range(len(st)):
		if st[i] in vowel:
			kevin += length - i
		else:
			stuart += length - i
	if kevin > stuart:
		print 'Kevin %s' % kevin
	if stuart > kevin:
		print 'Stuart %s' % stuart
	if stuart == kevin:
		print 'Draw'




#import string
#alpha = list(string.lowercase)
#vowel = list('aeiou')
#consonant = [i for i in alpha if i not in vowel]
#perm = []

#def permutation(x):
#    for i in range(len(x)):
#        check = [x[i:j] for j in range(i + 1, len(x) + 1)]
#        for k in check:
#            if k not in perm:
#                yield k

#def minion_game(st):
#    stuart = 0
#    kevin = 0
#    # this loop finds all unique permutations of the input string that need to be checked
#    instance = permutation(st)
#    condition = True
#    while condition:
#        try:
#            perm.append(next(instance))
#        except:
#            condition = False
#    # this loop tallies the score for stuart and kevin
#    for e in perm:
#        score = 0
#        for x in range(len(st) - len(e) + 1):
#            if e == st[x:x + len(e)]:
#                score += 1
#        if e[0].lower() in consonant:
#            stuart += score
#        elif e[0].lower() in vowel:
#            kevin += score

#    if stuart > kevin:
#        print 'Stuart %s' % stuart
#    elif stuart < kevin:
#        print 'Kevin %s' % kevin
#    elif stuart == kevin:
#        print 'Draw'

if __name__ == '__main__':
    s = raw_input()
    minion_game(s)
