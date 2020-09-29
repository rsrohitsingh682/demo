# Uses python3
import sys

def lcm_new(a, b):
    c = 0
    if(b == 0):
        return a
    c = a % b
    return lcm_new(b,c)    

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    c = (b // lcm_new(a,b)) * a
    print(c)

