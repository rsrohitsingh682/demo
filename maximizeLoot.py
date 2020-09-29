# Uses python3
import sys

def getMaxIndex(values, weights, n):
    index = -1
    max = 0
    for i in range(n):
        if (weights[i] > 0 and (values[i]/weights[i]) > max):
            max = values[i]/weights[i]
            index = i

    return index            


def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    n = len(weights)
    if(capacity == 0):
        return 0
    for i in range(n):
        maxIndex = getMaxIndex(values, weights, n)
        if maxIndex >= 0:
            available = min(capacity, weights[maxIndex])
            value = value + available * (values[maxIndex] / weights[maxIndex])
            weights[maxIndex] = weights[maxIndex] - available
            capacity = capacity - available    

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
   