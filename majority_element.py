# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    return -1

def majority_element_hashMap(a):
    n = len(a)
    m ={}
    for i in a:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1

    count = 0
    for key in m:
        if m[key] > n/2:
            count = 1
            print(1)
            break
    if count == 0:
       print(0)               


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # if get_majority_element(a, 0, n) != -1:
    #     print(1)
    # else:
    #     print(0)
    majority_element_hashMap(a)