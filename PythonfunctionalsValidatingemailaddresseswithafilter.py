def fun(s):
    name, web = [], []
    at, period = 0, 0
    for i in range(len(s)):
        if s[i] == '@':
            at = i
            break
        else:
            name.append(s[i])
    name = ''.join(name)
    for j in [x for x in range(len(s)) if x > at]:
        if s[j] == '.':
            period = j
            break
        else:
            web.append(s[j])
    web = ''.join(web)
    ext = s[period + 1:]
    condition = True
    parts = [name, web, ext]
    for e in parts:
        if len(e) == 0:
            condition = False
    for i in name:
        if not i.isalnum() and i not in ['-','_']:
            condition = False
    for i in web:
        if not i.isalnum():
            condition = False
    for i in ext:
        if not i.isalpha():
            condition = False
    if len(ext) > 3:
        condition = False
    return condition
    
    
    ########################## HACKERRANK CODE BELOW IS LOCKED ####################
    
    def filter_mail(emails):
    return filter(fun, emails)

if __name__ == '__main__':
    n = int(raw_input())
    emails = []
    for _ in range(n):
        emails.append(raw_input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print filtered_emails
