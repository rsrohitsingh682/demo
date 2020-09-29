#uses python 3
import sys

def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m*m):
        previous, current = current, (previous+current) % m

        #Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i+1

#calculation for Fn mod m
def fibonacciModulo(n,m):

    #Taking the mod of N with Pisano Period Length
     n = n % pisanoPeriod(m)

     previous, current = 0, 1
     if n == 0:
         return 0
     elif n == 1:
         return 1
     for i in range(n-1):
        previous, current = current, previous + current

     return current % m

#main code
if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(fibonacciModulo(n,m))
    
    #hello there#
            
