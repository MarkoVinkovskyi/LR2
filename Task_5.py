def f(num):
    m=0
    while num>0:
        m = m*10+num%10
        num = num//10
    return m
number = int(input())
print(f(number))