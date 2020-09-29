# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    index =0
    for i in range(1,n):
        if (numbers[i] > numbers[index]):
            index = i
    numbers[index], numbers[n] = numbers[n], numbers[index]
    index = 0
    for i in range(1,n-1):
        if (numbers[i] > numbers[index]):
            index = i
    numbers[index], numbers[n-1] = numbers[n-1], numbers[index]       
    return numbers[n-1]* numbers[n]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
