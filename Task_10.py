from functools import reduce

def calculate_average(numbers):
    non_zero_numbers = list(filter(lambda x: x != 0, numbers))
    return reduce(lambda x, y: x + y, non_zero_numbers) / len(non_zero_numbers)

def main():
    sequence = []
    while True:
        n = int(input())
        if n == 0:
            break
        sequence.append(n)
    print(calculate_average(sequence))

if __name__ == '__main__':
    main()
