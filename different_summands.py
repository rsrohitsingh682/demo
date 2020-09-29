# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    for i in range(1,n+1):
        if i*2 >= n:
            if n - i == 0:
                summands.append(i)
                break
        if i * 2 < n:
            summands.append(i)
            n = n - i

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
