fib_list = [0 ,1]
        
def fibonacci(n):
    if n == 0 or n == 1:
        return range(n)
    else:
        for i in range(2, n):
            fib_list.append(fib_list[i-1]+fib_list[i-2])
        return fib_list

cube = lambda x: x**3

################ HACKERRANK CODE LOCKED BELOW ############

if __name__ == '__main__':
    n = int(raw_input())
    print map(cube, fibonacci(n))
