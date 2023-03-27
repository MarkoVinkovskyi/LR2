def count_zeros_in_binary(n):
    binary_str = bin(n)[2:]
    zero_count = binary_str.count('0')
    return zero_count
print(count_zeros_in_binary(num))
