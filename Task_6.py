
def sum_binary_digits(num):

    binary_num = bin(num)[2:]
    return sum(int(digit) for digit in binary_num)

n = int(input())
sum_binary = sum_binary_digits(n)
print(sum_binary)
