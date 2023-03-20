def sum(num):
    if num.startswith('-'):
        sign = -1
        num = num[1:]
    else:
        sign = 1
    sum_of_digits=0
    for digit in num:
        sum_of_digits += int(digit)
    return sum_of_digits
number = input()
print(sum(number))