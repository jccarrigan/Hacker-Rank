N, nums = raw_input(), map(int, raw_input().split())

def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else: 
        return False

def is_neg(num):
    if num >= 0:
        return True
    else:
        return False
    
if all(map(is_neg, nums)):
    print any(map(is_palindrome, nums))
else:
    print False
