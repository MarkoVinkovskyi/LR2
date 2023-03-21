def f(num):
    m=0
    a=""
    if num<0 : a="-"
    num=abs(num)
    while num>0:
        m = m*10+num%10
        num = num//10
    return a+str(m)
number = int(input())
print(f(number))