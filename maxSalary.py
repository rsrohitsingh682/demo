#Uses python3

import sys

def largest_number(a):
    #write your code here
    res = ""
    i = 0
    while len(a) > 0:
        i = i + 1
        sMax = find_max_number(a)
        res += str(sMax)
        a.remove(sMax)
    return res

def find_max_number(a):
    max_ = a[0]
    for x in a:
        max_ = safe_max(max_, x)
    return max_

def safe_max(max_, x):
    A = str(max_) + str(x)
    B = str(x) + str(max_)
    if( A > B):
        return max_
    else:
        return x                

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
