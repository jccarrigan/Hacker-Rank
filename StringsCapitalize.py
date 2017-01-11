def capitalize(s):
    s = s[:].split(' ')
#    s = [((s[i][0]).upper() + s[i][1:]) for ((len(s[i]) > 0) and (i in range(len(s))))]
    for i in range(len(s)):
        if len(s[i]) > 0:
            s[i] = (s[i][0]).upper() + s[i][1:]
    return ' '.join(s)
    
    
    
    
    
if __name__ == '__main__':
    string = raw_input()
    capitalized_string = capitalize(string)
    print capitalized_string
