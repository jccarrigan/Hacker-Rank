for _ in range(input()):
    inp = raw_input().split()
    try:
        print int(inp[0])/int(inp[1])
    except Exception as e:
        print 'Error Code:', e
