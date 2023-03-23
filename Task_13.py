c=0
number = int(input())
while number != 0:
    if c<abs(number):
       c=number
    number = int(input())
print(c)